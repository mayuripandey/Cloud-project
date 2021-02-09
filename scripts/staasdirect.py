#!/usr/bin/python2

import commands
import cgi
print "content-type: text/html"

storage=cgi.FormContent()['store'][0]
if storage =="b_store":
	print "location: ../block_nfs.html"
else:
	print "location: ../nfs.html"   
print
