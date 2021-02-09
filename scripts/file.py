#!/usr/bin/python2

import cgi

print "Content-type: text/html"
print

print "<pre>"
print cgi.FormContent()['f'][0]
print "</pre>"
