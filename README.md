# ZAP-CMDLine
=============
Simple command line interface for automated security scanning with OWASP ZAP.

Introduction
-------------
This script performs the following steps:
1. Install PhantomJS using npm.
2. Start ZAP, set the AJAX spider browserId to phantomjs and pass the path to the PhantomJS binary.
3. Wait until ZAP is launched.
4. Start spidering, wait until complete.
5. Start AJAX spidering, wait until complete.
6. Start active scan, wailt until complete.
7. Write JSON results to disk.

Prerequisites
-------------
- Python must be installed.
- OWASP ZAP must be installed.
- zap.sh must be in the PATH for the current user.
- npm must be installed (used to install phantomjs)

Usage
-----
```
python zapcmd.py <url-of-site-to-scan> 
```

Jenkins integration
-------------------
You can integrate this script in a Jenkins job using the following steps:
1. Make sure that Python and npm are available on your Jenkins node(s).
2. (optional) Define a String parameter called TARGET_HOST to be able to choose the target host when starting the job.
3. Use the Custom Tools Plugin to download and install ZAP at build time.
4. Create a build step 'Execute shell' that executes the script:
```
python ./zapcmd.py ${TARGET_HOST}
```
5. Create a post-build action using the HTML Publisher Plugin that publishes report.html. 

Re-generating lib directory
---------------------------
```
wget https://bootstrap.pypa.io/get-pip.py && mkdir lib && python get-pip.py python-owasp-zap-v2.4 -t lib
```
