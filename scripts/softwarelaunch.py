#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"
print


service=cgi.FormContent()['software'][0]
ip=cgi.FormContent()['ipaddress'][0]
passw=cgi.FormContent()['pass'][0]


print commands.getstatusoutput('''echo -e "#!/usr/bin/python2\nimport commands\ncommands.getstatusoutput('export  DISPLAY=:0')\ncommands.getstatusoutput('sshpass -p redhat ssh -X -o stricthostkeychecking=no -l root 192.168.43.41 {}')" | cat > clientsoftgive.py'''.format(service))
commands.getstatusoutput("chmod +x *")
print commands.getstatusoutput("sudo sshpass -p {} scp clientsoftgive.py root@{}:Desktop".format(passw,ip))
#print commands.getstatusoutput("sshpass -p {} ssh -o stricthostkeychecking=no -l root {} python2 /root/Desktop/clientsoftgive.py".format(passw,ip))
print "successfully implanted software"
print """
<form action="../saas.html">
Go to prev page<input type="submit">
</form>
"""


