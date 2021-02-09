#!/usr/bin/python2
import commands
import cgi
print "content-type: text/html"
print 
print """


<body>
<textarea row=10 column=10 id="txtArea" onkeypress="onTestChange(event,this);"></textarea>
</body>


<script>
function onTestChange(e,textarea)
{
	var key=(e.keyCode?e.keyCode:e.which);
          if (key==13){
	alert(document.getElementById("txtArea").value);
        document.getElementById("txtArea").value=document.getElementById("txtArea").value+"   ";
}
}

</script>

"""
"""
document.getElementById("txtArea")
value=document.getElementById("txtArea").value+"\n*";
"""
