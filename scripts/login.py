#!/usr/bin/python2

import commands
import cgi


print "content-type: text/html"

username=cgi.FormContent()['username'][0]
password=cgi.FormContent()['password'][0]


auser="mukul"
apass="redhat"

if password != "":

	if auser == username and apass == password:
		print "location: ../menu.html"
		print

	else:
		print "location: ../login.html"
		print
else:
	print "location: ../login.html"
	print
	
