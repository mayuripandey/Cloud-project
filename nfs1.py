#!/usr/bin/python2
import commands
import cgi
print "Content-Type: text/html"
print 

serverIp=cgi.FormContent()['i'][0]
serverPassword=cgi.FormContent()['p'][0]
print "hello"
print "<pre>"
print serverIp
print serverPassword
vgStatus=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'vgdisplay myvg'".format(serverPassword,serverIp))

if(vgStatus[0]==0):
                 print vgStatus[1]
else:
    print "myvg is not present"
    commands.getoutput("exit")

userName=cgi.FormContent()['user'][0]

partsize=cgi.FormContent()['size'][0]

status=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'lvcreate --size {} --name {}-lv myvg'".format(serverPassword,serverIp,partsize,userName))


if(status[0]==0):
                print " succesfully created logical volume"
                vgStatus=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'lvdisplay /dev/myvg/{}-lv'".format(serverPassword,serverIp,userName))
                print vgStatus[1]

else:
    print status[1]

formatStatus=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'mkfs.ext4 /dev/myvg/{}-lv'".format(serverPassword,serverIp,userName))

commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'partprobe /dev/myvg/{}-lv'".format(serverPassword,serverIp,userName))

if(formatStatus[0]==0):
                      print "format succ"

else:
    print formatStatus[1]
    commands.getoutput("exit")

folderStatus=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'mkdir -p /share/{}-lv'".format(serverPassword,serverIp,userName))
if(folderStatus[0]==0):
                     print "/share/{}-lv folde is created".format(userName)
print "welcome"

mountStatus=commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} 'mount /dev/myvg/{2}-lv /share/{2}-lv'".format(serverPassword,serverIp,userName))

if(mountStatus[0]==0):
                   print "successfully mounted in /share/{}-lv1 folder".format(userName)

else:
   print mountStatus[1]
   commands.getoutput("exit")
str="/dev/myvg/{0}-lv /share/{0}-lv ext4 defaults 1 2".format(userName)
st=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'mkdir -p /copy'".format(serverPassword,serverIp))
if(st[0]==0):
     print "folder is created"
else:
    print "folder is not created"
# don't open a configure file in w mode 
st=commands.getstatusoutput("sshpass -p {1} sudo scp root@{0}:/etc/fstab /copy/".format(serverIp,serverPassword))
if(st[0]==0):
       print "copied"
else:
    print "not copied"

f=open("/copy/fstab",'a')
f.write(str+"\n")
f.close()
st=commands.getstatusoutput("sshpass -p {1} sudo scp /copy/fstab root@{0}:/etc/fstab".format(serverIp,serverPassword))
if(st[0]==0):
            print "fstab configure"
else:
        print "not configure"
clientIP=cgi.FormContent()['cip'][0]

clientPass=cgi.FormContent()['cpass'][0]

dirName=cgi.FormContent()['dirName'][0]
fstabStatus=commands.getstatusoutput("sshpass -p {1} ssh -o StrictHostKeyChecking=no -l root {0} 'mount -a'".format(serverIp,serverPassword))
if(fstabStatus[0]==0):
    print "succesfully configure in fstab"
else:
    print "there is some error plz check it mannually in /etc/fstab"

st=commands.getstatusoutput("echo -e '/share/{}-lv {}(rw,no_root_squash)' | sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'cat >> /etc/exports' ".format(userName,clientIP,serverPassword,serverIp))
print st
st=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'sudo systemctl restart nfs'".format(serverIp,serverPassword))
if(st[0]==0):
         print "nfs"
else:
   print "not nfs"
st=commands.getstatusoutput('''sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} "sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} mkdir -p /{}"'''.format(serverPassword,serverIp,clientPass,clientIP,dirName))
if(st[0]==0):
       print "directory client succ"
else:
      print "directory client not succ"
st=commands.getstatusoutput('''sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} "sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} mount {}:/share/{}-lv /{}"'''.format(serverPassword,serverIp,clientPass,clientIP,serverIp,userName,dirName))
if(st[0]==0):
          print "successfully mounted on client side"
else:
     print "not mmount"    
#client code
"""
st=commands.getstatusoutput('''sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} "sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} mkdir -p /{}"'''.format(serverIp,serverPassword,clientIP,clientPass,dirName))
if(st[0]==0):
       print "directory client succ"
else:
      print "directory client not succ"
st=commands.getstatusoutput('''sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} "sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} mount {}:/share/{}-lv /{}"'''.format(serverIp,serverPassword,clientIP,clientPass,serverIp,userName,dirName))
if(st[0]==0):
          print "successfully mounted on client side"
else:
     print "client side mount unsuccessfull"  

shareLocation="/share/{}-lv1 {}"+"\n".format(userName,clientIP)
"""
print "</pre>"
