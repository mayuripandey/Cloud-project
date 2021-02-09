#!/usr/bin/python2

import cgi
import commands

print "content-type:  text/html"
print



print """
<script>
function ls(sip)
{
document.location='iaasnext.py?ip='+sip
}

</script>
"""


print """
<script>
function ls1()
{
document.location='iaasmanage.py'
}

</script>
"""









ServerIP=cgi.FormContent()['ipaddress'][0]
passd=cgi.FormContent()['passd'][0]
osname=cgi.FormContent()['osname'][0]
ostype=cgi.FormContent()['ostype'][0]
cpunumber=cgi.FormContent()['cpunumber'][0]
storagesize=cgi.FormContent()['storagesize'][0]
ramsize=cgi.FormContent()['ramsize'][0]



ossetup="virt-install --name  {0} --location  /os/rhel-server-7.3-x86_64-dvd.iso  --os-type   linux  --os-variant {1} --memory  {4} --vcpus  {2} --disk  /var/lib/libvirt/images/{0}.qcow2,size={3} --graphics  vnc,listen=0.0.0.0,port=5903  --noautoconsole".format(osname,ostype,cpunumber,storagesize,ramsize)

ossetupstatus=commands.getstatusoutput("sudo sshpass -p {} ssh -o stricthostkeychecking=no {} {}".format(passd,ServerIP,ossetup))

if ossetupstatus[0] == 0:
	print "Your os setup is done"
else:
	print ossetupstatus[1]

"""
a=commands.getstatusoutput(" cd /webcontent/novnc/utils && ./launch.sh 192.168.43.177:5901")
b=commands.getstatusoutput(" cd /webcontent/websockify-master/ &&  ./run 192.168.43.143:1234 192.168.43.177:5901")
print a[1]
print b[1]"""
print "<button onclick=ls('{}')>CLick here to get your os in the browser</button>".format(ServerIP)
print "<button onclick=ls1()>Manage your os</button>"












