#!/usr/bin/python2



import cgi
print "Content-type: text/html"

cmd=cgi.FormContent()['serv'][0]


if cmd == "docker":
	print "location: ../docker.html"
	print
else:
	print
	print "sorry page not yet ready"
