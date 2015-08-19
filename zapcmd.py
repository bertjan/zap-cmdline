#!/usr/bin/env python

import subprocess
import time
import json
import sys
sys.path.append("./lib")
from zapv2 import ZAPv2

# Check command line arguments.
if len (sys.argv) < 2:
    print 'Pass the URL of the site to scan as (only) parameter.'
    sys.exit(2)

# Use first parameter as URL to scan.
target = sys.argv[1]
zap = ZAPv2()

# Start zap.
print 'Starting ZAP.'
subprocess.Popen(['zap.sh','-daemon','-config','api.disablekey=true'])
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
zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)


# Spider the target.
print 'Spidering target %s' % target
zap.spider.scan(target)
# Give the Spider a chance to start
time.sleep(2)
while (int(zap.spider.status()) < 100):
    print 'Spider progress %: ' + zap.spider.status()
    time.sleep(2)

print 'Spider completed'
# Give the passive scanner a chance to finish
time.sleep(5)


# Start AJAX spider.
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

# Print results to console.
print results

# Write the results to disk.
f = open('report.json', 'w')
f.write(str(results))
f.close()

# Shutdown ZAP.
zap.core.shutdown()

