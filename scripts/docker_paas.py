#!/usr/bin/python2

import cgi 
import commands

print "content-type: text/html"
print 


print """
<script>
function run(cv)
{

cmd=document.getElementById('txtArea').value
document.location='docker_comm.py?cName='+cv+'&comd='+cmd
}

</script>
"""


print """
<script>
function onTestChange(e,textarea)
{
	var key=(e.keyCode?e.keyCode:e.which);
          if (key==13){
	alert(document.getElementById("txtArea").value);
        document.getElementById("txtArea").value=document.getElementById("txtArea").value+"1";
}
}

</script>
"""







cname=cgi.FormContent()['cName'][0]
print "Container Name:"+cname 
print """<h2> Enter your centos commands below </h2>
<form >
<textarea rows="15" cols="70" id="txtArea" onkeypress="onTestChange(event,this);">
</textarea><br/><br/>"""
print "<input value='Run' type='button' onclick=run('"+cname+"') />"
print "</form>"
