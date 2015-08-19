# ZAP-CMDLine
=============
Simple command line interface for automated security scanning with OWASP ZAP.

Introduction
-------------
TODO.

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

Re-generating lib directory
---------------------------
```
wget https://bootstrap.pypa.io/get-pip.py && mkdir lib && python get-pip.py python-owasp-zap-v2.4 -t lib
```
