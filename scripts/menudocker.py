#!/usr/bin/python2

import commands
import cgi
print "content-type: text/html"
print

import newdocker



print "<form action='/scripts/dockerlaunch.py'>"
print "Run your commands!!- <br/>"
print "Below are some os <br/>"
newdocker.images()
print "Enter name of container"
print "<input type='text' name='c_name'/>"
print "<input type='submit' value='Run'/> <br/>"
print "</form><br/>"

"""
print "<form action='/scripts/manage.py'>"
print "Manage your containers"
print "<input type='submit' value='manage'/>"
print "</form><br/>"


print "<form action='/scripts/download.py'>"
print "Search and download container<br/>"
print "<input type='text' name='osname'/>"
print "<input type='submit' value='Search'/>"
print "</form><br/>"

"""
print "<h3>Configure your container: </h3>"
print "<form action='caasdocker.py'>"

print "Enter no of containers <input type='text' name='noc' /><br/>"
print "IP address of the system<input type='text' name='ipaddress'/><br/><br/>"
print "Enter Password <input type='password' name='passwd' /><br/>"
print "Select os:"
newdocker.images()

print "Select services:<br/>"
print "Enter Name Of Service<input type='text' name='serv2' />"
print "<br/> <br/>Create a tar  file out of it<input type='checkbox' name='tar'/>"
print "<br/><br/><input type='submit' value='Submit'/>"
print "</form>"



