#!/usr/bin/python2

import commands

def images():
	images=commands.getstatusoutput("sudo docker images")
	str=images[1].split('\n')
	print "<pre>"
	z=1
	print "<select name='os'>" 
	for i in str:
		if z==1:
			pass
		else:
			print "<option value='{0}:{1}'> {0}:{1} </option>".format(i.split()[0],i.split()[1])
		z=z+1
	print "</select>"
	print "</pre>"






def search(searchimg):
	#searchname=cgi.FormContent()['osname'][0]
	searchname=commands.getstatusoutput("sudo docker search {}".format(searchimg))
	str=searchname[1].split('\n')
	print "<pre>"
	z=1
	print "<select name='os'>" 
	for i in str:
		if z==1:
			pass
		else:
			print "<option value='{0}:{1}'> {0}:{1} </option>".format(i.split()[0],i.split()[1])
		z=z+1
	print "</select>"
	print "</pre>"



