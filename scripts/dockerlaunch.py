#!/usr/bin/python2

import cgi 
import commands

print "content-type: text/html"
print


print """
<script>
function lw1(cname)
{
alert(cname+' Name Alreday Exists')
document.location='menudocker.py?serv=docker'
}

</script>
"""



print """
<script>
function lw2(cname)
{
alert(cname+': Docker launched')
document.location='menudocker.py?serv=docker'
}

</script>
"""



imageName=cgi.FormContent()["os"][0]
cName=cgi.FormContent()["c_name"][0]

if commands.getstatusoutput("sudo docker inspect {}".format(cName))[0]==0:
	print "docker exist"
else:
	    commands.getstatusoutput("sudo docker run -dit --name {0} {1}".format(cName,imageName))
	    print "docker launch"

