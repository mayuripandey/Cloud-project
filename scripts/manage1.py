#!/usr/bin/python2
import commands
import cgi
print "content-type: text/html"
service=cgi.FormContent()['service'][0]


if service=="manage":
	print "location: manage.py"
else:
	print "location: menudocker.py"

print

