#!/usr/bin/python

import cgi 
import commands

print "content-type: text/html"
 
vname=cgi.FormContent()['cName'][0]
commands.getoutput("sudo virsh start {}".format(vname))

print "location: iaasmanage.py"
print
