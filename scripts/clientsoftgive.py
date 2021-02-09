#!/usr/bin/python2
import commands
commands.getstatusoutput('export  DISPLAY=:0')
commands.getstatusoutput('sshpass -p redhat ssh -X -o stricthostkeychecking=no -l root 192.168.43.41 firefox')
