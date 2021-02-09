#!/usr/bin/python2
import commands
import cgi
print "Content-Type: text/html"
print 

serverIp=cgi.FormContent()['i'][0]
serverPassword=cgi.FormContent()['p'][0]
clientIP=cgi.FormContent()['cip'][0]

clientPass=cgi.FormContent()['cpass'][0]

userName=cgi.FormContent()['user'][0]

partsize=cgi.FormContent()['size'][0]

print "<pre>"
print serverIp
print serverPassword
vgStatus=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'vgdisplay myvg'".format(serverPassword,serverIp))

if(vgStatus[0]==0):
                 print vgStatus[1]
else:
    print "myvg is not present"+vgStatus[1]
    commands.getoutput("exit")
status=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'lvcreate --size {} --name {} myvg'".format(serverPassword,serverIp,partsize,userName))


if(status[0]==0):
                print " succesfully created logical volume"
                vgStatus=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'lvdisplay /dev/myvg/{}'".format(serverPassword,serverIp,userName))
                print vgStatus[1]

else:
    print status[1]
st=commands.getstatusoutput("sudo mkdir -p /copy")
if(st[0]==0):
     print "folder is created"
else:
    print "folder is not created"
# don't open a configure file in w mode 
st=commands.getstatusoutput("sshpass -p {0} sudo scp root@{1}:/etc/tgt/targets.conf /copy/".format(serverPassword,serverIp))
if(st[0]==0):
       print "copied"
else:
    print "not copied"
str="<target {0}>\n backing-store /dev/myvg/{1} \n</target>".format(userName,userName)
print "hello"
f=open("/copy/targets.conf",'a')
print "hello"
f.write(str+"\n")
f.close()
st=commands.getstatusoutput("sudo sshpass -p {} scp /copy/targets.conf root@{}:/etc/tgt/targets.conf".format(serverPassword,serverIp))
if(st[0]==0):
            print "tgt configure"
else:
        print st[1]
fstabStatus=commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} 'systemctl restart tgtd'".format(serverPassword,serverIp))
if(fstabStatus[0]==0):
    print "succesfully start tgt"
else:
    print "not tgt start "

st=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'tgt-admin -show' ".format(serverPassword,serverIp))
print st[1]
st=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'chkconfig on'".format(serverPassword,serverIp))
if(st[0]==0):
         print "check configure is on "
else:
   print "check configure is not on"
st=commands.getstatusoutput('''sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} "iptables -F" '''.format(serverPassword,serverIp))
if(st[0]==0):
       print "firewall is off"
else:
      print "firewall is not off"

discoverstatus=commands.getstatusoutput("sudo sshpass -p {} ssh -o stricthostkeychecking=no {}   iscsiadm --mode discoverydb --type sendtargets --portal {} --discover".format(clientPass,clientIP,serverIp))
print discoverstatus
print
loginstatus=commands.getstatusoutput("sudo sshpass -p {} ssh -o stricthostkeychecking=no {} 'iscsiadm --mode node --targetname {} --portal {}:3260 --login'".format(clientPass,clientIP,userName,serverIp))
print loginstatus
print "</pre>"
