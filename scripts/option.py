#!/usr/bin/python2
import commands
import cgi
print "content-type: text/html"
print

print "<center><h1>Container Services</h1></center>"
print """
<body bgcolor="#00BFFF">
<center>
<form action='manage1.py'>
Manage Container<input type='radio' name='service' value='manage' /></br></br>
Launch Container<input type='radio' name='service' value='launch' /></br></br>
<input type='submit' value='submit' />
</center>
</form>
</body>
"""
