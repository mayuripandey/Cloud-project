#!/usr/bin/python2

import commands
import cgi
import newdocker
print "content-type: text/html"
print

osname=cgi.FormContent()['osname'][0]
print "<h2>Search Results</h2>"

print "<form action='/scripts/dwnldrederict.py'>"
newdocker.search(osname)
print "<input type='submit' value='Download'/>"
print "</form><br/>"



