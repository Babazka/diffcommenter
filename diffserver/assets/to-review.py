
from subprocess import Popen, PIPE
import os
import sys
import urllib
import urllib2


CLIENT_VERSION = None
    sha1, ref = out.strip().split(' ', 1)
        'client_version': str(CLIENT_VERSION),
    try:
        print urllib2.urlopen(url, urllib.urlencode(data)).read()
    except urllib2.HTTPError as err:
        code = err.getcode()
        print 'HTTP Error code: ', code
        if code == 400:
            print err.read()