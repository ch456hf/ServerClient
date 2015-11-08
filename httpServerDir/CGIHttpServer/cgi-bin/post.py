#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()

print "Content-Type: text/html"
print
print "<p>Hello world!</p>"
print "<p>" + repr(form['firstname']) + "</p>"
