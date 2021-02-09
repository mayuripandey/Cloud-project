#!/usr/bin/python2
import cgi
import cgitb
import commands
print "Content-type: text/html"


size=cgi.FormContent()['size'][0]
name=cgi.FormContent()['name'][0]
ipaddress=cgi.FormContent()['ipaddress'][0]
password=cgi.FormContent()['password'][0] 
print "set-cookie: p={}".format(password)
print
create=commands.getstatusoutput("sudo lvcreate --size {} --name {} myvg".format(size,name))
if create[0]==0:
	print "created"

commands.getstatusoutput(" sudo echo -e '<target {0}>\n backing-store /dev/myvg/{0} \n</target>\' | cat >> /etc/tgt/targets.conf".format(name))
commands.getstatusoutput("sudo systemctl restart tgtd")
commands.getstatusoutput("sudo echo '{} ansible_ssh_user=root ansible_ssh_pass={}' |  cat >> /etc/ansible/hosts".format(ipaddress,password))
ansiblestatus=commands.getstatusoutput("sudo ansible-playbook scsi.yml")
print ansiblestatus
print
discoverstatus=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1}  iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.143 --discover".format(password,ipaddress))
print discoverstatus
print
loginstatus=commands.getstatusoutput("sudo sshpass -p {} ssh -o stricthostkeychecking=no {} 'iscsiadm --mode node --targetname {} --portal 192.168.43.143 --login'".format(password,ipaddress,name))
print loginstatus







