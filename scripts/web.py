#!/usr/bin/python2

import cgi

import commands

print "Content-Type: text/html"
print

ipaddress=cgi.FormContent()['ip'][0]
package=cgi.FormContent()['pack'][0]

packagestatus=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} 'rpm -q {1}'".format(ipaddress,package))
if packagestatus[0]==0:
	print "already installed.."
else:
	softwarestatus=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} 'yum install {1} -y'".format(ipaddress,package))
	if softwarestatus[0]==0:
		print "successfully installed"
	else:
		print "try again"
