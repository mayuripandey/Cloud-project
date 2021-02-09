#!/usr/bin/python2
import cgitb
import cgi
import commands
print "Content-type: text/html"
print 
cgitb.enable(display=1, logdir=None,context=5,format='html')
cmd=cgi.FormContent()['comd'][0]



multicmd= cmd.split("1")

z=1
for i in multicmd:
	if z==1:
		z=z+1		
		f=open("/webcontent/scripts/pythonx.py","a")  
		f.write("#!/usr/bin/python2") 
		f.close()
	if i!="": 
		
		f=open("/webcontent/scripts/pythonx.py","a")  
		f.write("\n{}\n".format(i))  
f.close()
x=commands.getstatusoutput("python /webcontent/scripts/pythonx.py") 
print "<pre>"
print x[1]
print "</pre>"
f=open("/webcontent/scripts/pythonx.py","w") 
f.close() 
cgitb.enable(display=1, logdir=None,context=5,format='html')

