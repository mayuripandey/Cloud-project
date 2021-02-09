#!/usr/bin/python

import cgi 
import commands

print "content-type: text/html"
print

print """
<script>
function start(cv)
{
alert(cv)
document.location='iaasstart.py?cName='+cv
}

</script>
"""



print """
<script>
function stop(cv)
{
alert(cv)
document.location='iaasstop.py?cName='+cv
}

</script>
"""





print """
<script>
function remo(cv)
{
alert(cv)
document.location='iaasremove.py?cName='+cv
}

</script>
"""




z=1
print "<table border='4'>"
print "<tr><th>Name</th><th>Status</th><th>Stop</th><th>Start</th> <th>Remove</th></tr>"

for i in commands.getoutput("sudo virsh list --all").split('\n') :
            if z<=2:
		pass
		
	    else:	
		j=i.split()
 	    
		print "<tr><td> <input value='"+j[1]+"'type='button'/> </td><td>"+j[2]+"</td><td><button onclick=stop('"+j[1]+"')>Stop<button /></td><td><button onclick=start('"+j[1]+"')>Start</button></td><td><button onclick=remo('"+j[1]+"')>Remove</button></td></tr>"
	    z=z+1

print "</table> " 

