#! /bin/env python
from urllib import urlopen, urlretrieve
from urlparse import urlparse
from os import system
from os.path import expanduser
import re

CHANNEL="http://www.sublimetext.com/dev"
PLATFORM="Linux 64 bit"
INSTALL_DIR="~/src/"

INSTALL_DIR = expanduser(INSTALL_DIR)

url = re.search(r'<a href="([^"]*)">%s</a>' % PLATFORM, 
        urlopen(CHANNEL).read()).groups(0)[0]

fn = urlparse(url).path
print "Fetching '%s'" % url
urlretrieve(url, "/tmp" + fn)
cmd = 'tar xjf "/tmp{0}" -C "{1}"'.format(fn, INSTALL_DIR)
system('rm -r "%s/Sublime Text 2"' % INSTALL_DIR)
print "Unpacking to %s " % INSTALL_DIR
system(cmd)