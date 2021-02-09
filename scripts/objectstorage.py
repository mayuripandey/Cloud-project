#!/usr/bin/python2

import commands
import getpass
import cgi
print "Content-type: text/html"
print

size=cgi.FormContent()['size'][0]
name=cgi.FormContent()['name'][0]
ipaddress=cgi.FormContent()['ipaddress'][0]
password=cgi.FormContent()['password'][0] 
dirname=cgi.FormContent()['dirname'][0]

create=commands.getstatusoutput("sudo lvcreate --size {} --name {} myvg".format(size,name))

if create[0]==0:
	print "created"


print commands.getstatusoutput("sudo mkdir /{} ".format(dirname))

print commands.getstatusoutput("ansible-playbook obgstarage.yml")
print commands.getstatusoutput("sudo mkfs.ext4 /dev/myvg/{}".format(name))
print commands.getstatusoutput("sudo chmod 666 /dev/myvg/{}".format(name))
print commands.getstatusoutput("sudo chmod 666 /{}".format(dirname))
print commands.getstatusoutput("sudo mount /dev/myvg/{} /{} ".format(name,dirname))
print commands.getstatusoutput("sudo chown apache /etc/exports") 
print commands.getstatusoutput("sudo echo '/{} {}' | cat >> /etc/exports".format(name,ipaddress))
print commands.getstatusoutput("sudo systemctl restart nfs")

print commands.getstatusoutput("sudo sshpass -p {} ssh -o stricthostkeychecking=no {} 'mkdir /{}' ".format(password,ipaddress,dirname))



#commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} 'mount 192.168.43.143:/{2} /{2} ".format(password,ipaddress,dirname))
















