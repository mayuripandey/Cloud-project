#!/usr/bin/python2
import cgi
import commands
print "Content-type: text/html"

os=cgi.FormContent()['os'][0]
dockerstatus=commands.getstatusoutput("sudo docker run -dit --name nikhil-{}-1 centos:latest".format(os))
if dockerstatus[0]==0:
	print "location: ../docker_comm.html"
	print 
