#!/usr/bin/python

import cgi 
import commands

print "content-type: text/html"
print 

print """
<script>
function lw(cv)
{
alert(cv)
document.location='docker_remove.py?cName='+cv
}

</script>
"""
print """
<script>
function sp(cv)
{
alert(cv)
document.location='docker_stop.py?cName='+cv
}

</script>
"""
print """
<script>
function st(cv)
{
alert(cv)
document.location='docker_start.py?cName='+cv
}

</script>
"""


print """
<script>
function ps(cv)
{
alert(cv)
document.location='docker_paas.py?cName='+cv
}

</script>
"""
print "<table border='5'>"
print "<tr><th> image_Name</th>"
print "<th> c_name</th>"
print "<th> Status</th>"
print "<th> Stop</th>"
print "<th> Start</th>"
print "<th> Remove</th></tr>"

z=1
#print commands.getoutput("sudo docker ps -a").split('\n')[2].split()[1]

for i in commands.getoutput("sudo docker ps -a").split('\n') :
            if z==1:
		z+=1
		
	    else:	
		j=i.split()
		cStatus=commands.getoutput("sudo docker inspect {0}|jq '.[].State.Status'".format(j[-1]))
		print "<tr><td>"+j[1]+"</td><td><input value='"+j[-1]+"'type='button' onclick=ps('"+j[-1]+"') /></td><td>"+cStatus+"</td><td><button onclick=sp('"+j[-1]+"')>Stop<button /></td><td><button onclick=st('"+j[-1]+"')>Start<button /></td><td><input value='"+j[-1]+"'type='button' onclick=lw('"+j[-1]+"') /></td></tr>"


print "</table>"

