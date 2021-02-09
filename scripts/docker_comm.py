#!/usr/bin/python2
import cgi
import commands
print "Content-type: text/html"
print

cname=cgi.FormContent()['cName'][0]
cmd=cgi.FormContent()['comd'][0]


cmdstatus=commands.getstatusoutput("sudo docker start " +cname)

if cmdstatus[0]!=0:
	print cmdstatus[1]+"\n"


multicmd= cmd.split("1")

print "<pre>"
for i in multicmd:
	#newcmd=i.strip("\n")
	if i!="":
		print i+":\n"
		cmdstatus=commands.getstatusoutput("sudo docker exec {} {}".format(cname,i))
		if cmdstatus[0]==0:
			print cmdstatus[1]+"\n"
		else:
			print cmdstatus[1]
		print "\n"
	else:
		pass

print "</pre>"



print "<br/><br/>"
print "<a href=docker_paas.py?cName="+cname+">Click here to go back</a>"

