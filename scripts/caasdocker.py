#!/usr/bin/python2

import commands

import cgi

print "content-type: text/html"
print

noc=cgi.FormContent()['noc'][0]
passwd=cgi.FormContent()['passwd'][0]
ipaddress=cgi.FormContent()['ipaddress'][0]
os=cgi.FormContent()['os'][0]
tar=cgi.FormContent()['tar'][0]
serv2=cgi.FormContent()['serv2'][0]
print serv2


inststatus=commands.getstatusoutput("sudo docker exec mukul1 yum install {} -y".format(serv2))
if inststatus==0:
	print "done"
else:
	print "enter correct name"
 
dockercomstat=commands.getstatusoutput("sudo docker commit mukul1 {}image".format(serv2))
print dockercomstat

dockersavestat=commands.getstatusoutput("sudo docker save  -o {}.tar {}image ".format(ipaddress,serv2))
print dockersavestat

dockerscp=commands.getstatusoutput("sudo sshpass -p {} scp 192.168.43.177.tar root@{}:Desktop  ".format(passwd,ipaddress))
print dockerscp





