#!/usr/bin/python2

import cgi 
import commands

print "content-type: text/html"
 


cName=cgi.FormContent()['cName'][0]
#print cgi.FormContent()['cName'][0]

removeStatus=commands.getstatusoutput("sudo docker start {}".format(cName))



print "location: manage.py"
print


