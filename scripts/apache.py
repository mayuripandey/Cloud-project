#!/usr/bin/python2
import commands
import cgi
print "content-type: text/html"
print
webserver_portno = cgi.FormContent()['port'][0]
webserver_dir = cgi.FormContent()['dir'][0]
ServerIp = cgi.FormContent()['ip'][0]
ServerPass = cgi.FormContent()['pass'][0]
ConfigFile = cgi.FormContent()['conffile'][0]
print "hello"
web_server = commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} rpm -q httpd".format(ServerPass, ServerIp))
if web_server[0] == 0:
	print "software is already installed"
else:
	print "Software is installing.... "
	soft_install = commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} yum install httpd -y".format(ServerPass, ServerIp))
	if soft_install[0] == 0:
		print "software successfully installed"
	else:
		print "ERROR..!"
# step 2: configure file 
 
conf_file = commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} touch /etc/httpd/conf.d/{2}.conf".format(ServerPass, ServerIp, ConfigFile))
if  conf_file[0] == 0:
	print "conf file created "
else:
	print "Command Error.." 

deploy_dir = commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} mkdir -p /{2}".format(ServerPass, ServerIp, webserver_dir))
if deploy_dir[0] == 0:
	print "Deployment Directory created .."
else:
	print "ERROR.."

web_server_configure = commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1}   'echo -e \"Listen {2}\nDocumentroot /'{3}'\n<Directory {3}>\nrequire all granted\n</Directory>\" >/etc/httpd/conf.d/{4}.conf'".format(ServerPass, ServerIp, webserver_portno, webserver_dir, ConfigFile))
if web_server_configure[0] == 0:
	print "web server configured"
else:
	print "Error in content of conf file..."
	print "Error" 

commands.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} setenforce 0".format(ServerPass, ServerIp))
commands.getoutput("sshpass -p {0} sudo scp /web/index.html root@{1}:{2}".format(ServerPass, ServerIp, webserver_dir))

#step 3:  Start Daemon (Service)
start_service = commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} systemctl restart httpd".format(ServerPass, ServerIp))
if start_service[0] == 0:
	print "httpd service started .."
else:
	print "Service not started..Restart service! "

commands.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} systemctl stop firewalld".format(ServerPass, ServerIp))
