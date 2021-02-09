#!/usr/bin/python2
import commands
import cgi
print "content-type: text/html"
service=cgi.FormContent()['serv'][0]
if service=="saas":
	print "location: ../saas.html"
elif service=="staas":
	print "location: ../staasmenu.html"
elif service=="caas":
	print "location: option.py"
elif service=="iaas":
	print "location: ../iaas.html"
elif service=="paas":
	print "location: menupaas.py"
else:
	print "location: ../webserver.html"

print
