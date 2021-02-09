#!/usr/bin/python2

import commands
import os
import cgi

print "content-type: text/html"
print
nos=os.environ['HTTP_COOKIE']
service=nos.split('=')
no_service=int(service[1])
i=1
while i <= no_service:
	cmd=cgi.FormContent()['text{}'.format(i)][0]
	print cmd
	print commands.getstatusoutput("sudo sshpass -p redhat  ssh -o stricthostkeychecking=no 192.168.43.143 ' docker exec nikhil-centos-1 yum install {} -y' ".format(cmd))
	i=i+1 
