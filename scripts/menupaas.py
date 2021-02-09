#!/usr/bin/python2

import commands
import cgi
print "content-type: text/html"
print

import newdocker
print """
<script>
function shell()
{
x=document.getElementById('txt').value
alert(x)
document.location="https://"+x+":4200"
}
</script>

"""

print "<br/>"
print "<h2>Shell in a box<h2>"
print "<h2>Enter the IP Address Below </h2>"
print """

<textarea id="txt" row="3"></textarea>
<button onclick='shell()'>Get Shell</button>
<br/>
<h2> Or, You can use Python Terminal<h2>


"""


print """
	<form action='pythonexe.py'>
        <h3> Python Terminal: </h3>
       <input type='submit' value='For Python Terminal Click Here'/>
	</form>
"""





