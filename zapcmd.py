#!/usr/bin/env python

import sys
sys.path.insert(1, "./lib")
import subprocess
import os
import time
import json
import string
from zapv2 import ZAPv2

# Check command line arguments.
if len (sys.argv) < 2:
    print 'Pass the URL of the site to scan as first parameter.'
    print 'Optionally, pass http username and password as 2nd and 3rd parameter.'
    sys.exit(2)

# Use first parameter as URL to scan.
target = sys.argv[1]
httpUsername = None
httpPassword = None
if len (sys.argv) == 4:
    httpUsername = sys.argv[2]
    httpPassword = sys.argv[3]
    target = string.replace(target, '://', '://' + httpUsername + ':' + httpPassword + '@')
zap = ZAPv2()

# Configuration
browser='firefox'
#browser='phantomjs'

# chdir to path of the script to make sure that PhantomJS is installed relatively to the script path.
scriptPath=os.path.abspath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

# Install PhantomJS.
print 'Installing PhantomJS to support AJAX spidering.'
subprocess.call(['npm','install','phantomjs'])

phantomJSPath=scriptPath + '/node_modules/phantomjs/bin/phantomjs'
print 'Using PhantomJS binary path ' + phantomJSPath

# Start zap.
print 'Starting ZAP.'
subprocess.Popen(['zap.sh','-daemon','-config','api.disablekey=true','-config','ajaxSpider.browserId='+browser,'-config','selenium.phantomJsBinary=' + phantomJSPath])

print 'Waiting for ZAP to load.'

# Wait until the ZAP API is reachable.
version = ''
while (version == ''):
    try:
        version=zap.core.version
    except:
        print 'ZAP not running yet, waiting.'
        time.sleep(1)
    else:
        # Wait a bit more for ZAP to fully start.
        time.sleep(1)

# Ready for business ;-)
print 'ZAP version ' + version + ' is running.'

# Connect to the target.
print 'Accessing target %s' % target
htmlResult = zap.urlopenWithPassword(target, httpUsername, httpPassword)
print 'Received HTML: ' + htmlResult

# Give the sites tree a chance to get updated
time.sleep(2)

# Spider the target.
print 'Spidering target %s' % target
zap.spider.scan(target)
time.sleep(2)
while (int(zap.spider.status()) < 100):
    print 'Spider progress %: ' + zap.spider.status()
    time.sleep(2)

print 'Spider completed'
# Give the spider some time to finish.
time.sleep(2)


# Start the AJAX spider.
print 'AJAX spidering target %s' % target
zap.ajaxSpider.scan(target)

# Wait for AJAX spider to complete.
while (zap.ajaxSpider.status != 'stopped'):
    print 'AJAX spider ' + zap.ajaxSpider.status + ', ' + zap.ajaxSpider.number_of_results + ' results.'
    time.sleep(1)

print 'AJAX Spider completed'
# Give the AJAX spider some time to finish.
time.sleep(3)

print 'Scanning target %s' % target
zap.ascan.scan(target)
while (int(zap.ascan.status()) < 100):
    print 'Scan progress %: ' + zap.ascan.status()
    time.sleep(5)

print 'Scan completed'

# Gather results.
results = json.dumps(zap.core.alerts())

# Log results to console.
print results

# Write the results to disk.
f = open('report.json', 'w')
f.write(str(results))
f.close()

# Shutdown ZAP.
zap.core.shutdown()

