# ZAP-CMDLine
=============
Simple command line interface for automated headless security scanning with OWASP ZAP and PhantomJS.

Introduction
-------------
This script performs the following steps:

1. Install PhantomJS using npm.
2. Start ZAP, tell it to use PhantomJS for AJAX spidering.
3. Wait until ZAP is launched.
4. Start spidering, wait until complete.
5. Start AJAX spidering, wait until complete.
6. Start active scan, wailt until complete.
7. Write JSON results to disk.

This script has been tested on OSX 10.10.4 and on Amazon Linux 2015.03.
Running on Windows should work with a few minor adjustments.

Prerequisites
-------------
- Python must be installed (tested with Python 2.6.9 and 2.7.10)
- OWASP ZAP must be installed (tested with ZAP 2.4.1)
- zap.sh must be in the PATH for the current user.
- npm must be installed and in the PATH (used to install PhantomJS)

Usage
-----
Syntax:
```
python zapcmd.py <url-of-site-to-scan> 
```

Example:
```
python zapcmd.py http://www.example-site-to-scan.com
```


Jenkins integration
-------------------
You can integrate this script in a Jenkins job with the following steps:

1. Make sure that Python and npm are available on your Jenkins node(s).
2. (optional) Define a String parameter called TARGET_HOST to be able to choose the target host when starting the job.
3. Use the Custom Tools Plugin [Custom Tools Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Custom+Tools+Plugin) to download and install ZAP at build time. See [here](https://wiki.jenkins-ci.org/display/JENKINS/ZAProxy+Plugin) for instructions.
4. Create a build step 'Execute shell' that executes the script: `python ./zapcmd.py ${TARGET_HOST}`
5. Create a post-build action using the [HTML Publisher Plugin](https://wiki.jenkins-ci.org/display/JENKINS/HTML+Publisher+Plugin) that publishes report.html. 

Packaged dependencies
---------------------------------
This repository contains two folders with packaged dependencies for ease of use.

The 'lib' folder contains the OWASP ZAP Python API. You can re-generate the folder with the following command:
```
wget https://bootstrap.pypa.io/get-pip.py && mkdir lib && python get-pip.py python-owasp-zap-v2.4 -t lib
```

The 'web' folder contains a local copy of the jQuery, Bootstrap and the [jPut](https://shabeer-ali-m.github.io/jPut) JSON rendering jQuery plugin.
