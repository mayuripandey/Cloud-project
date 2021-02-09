#!/usr/bin/python2

import cgi 
import commands 
print "content-type: text/html"
print 
print """<h2> Enter your PYTHON COMMANDS BELOW </h2>
<form >
<textarea rows="15" cols="70" id="txtArea" onkeypress="onTestChange(event,this);">
</textarea><br/><br/>""" 
print "<input value='Run' type='button' onclick=run() />"
print "</form>"
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
print """
<script>
function run()
{

cmd=document.getElementById('txtArea').value
document.location='python_comm.py?comd='+cmd

} 


</script>
"""
