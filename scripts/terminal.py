#!/usr/bin/python2
import commands
import cgi

print "Content-Type: text/html"
print
ip=cgi.FormContent()['t'][0]
print ip
print """
<script>
function lw(x)
{
alert(x)
document.location="https://"+x+":4200"
}
</script>
"""
print "<button onclick=lw('{}')>click me</button>".format(ip)

