#!/usr/bin/python2

import commands

print "Content-type: text/html"
print

print commands.getstatusoutput("export DISPLAY=:0")
print commands.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -X 192.168.43.143 firefox")
