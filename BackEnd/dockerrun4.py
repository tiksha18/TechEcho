#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
osname = form.getvalue("x")

cmd = "sudo docker stop {}".format(osname)
print("O.S./Container named - {}, has been stopped successfully".format(osname))
