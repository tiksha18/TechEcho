#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
cmd = form.getvalue("t")

if(("cal" in cmd) or ("command" in cmd) or ("calendar" in cmd)):
  print(sp.getoutput("sudo cal"))
elif(("date" in cmd) or ("command" in cmd) or ("time" in cmd)):
  print("Date :")
  print(sp.getoutput("sudo date"))
elif((("current status" in cmd) or ("status" in cmd)) and (("httpd" in cmd) or ("web server" in cmd))):
  print(sp.getoutput("sudo systemctl status httpd"))
elif((("list" in cmd) or ("show" in cmd)) and (("packages" in cmd) or ("version" in cmd))):
  print("List of all installed packages :")
  print(sp.getoutput("sudo pip3 list"))
elif(("who am I" in cmd) or ("who I am" in cmd) or ("what is my name" in cmd) or ("name" in cmd)):
  print("I  am " + (sp.getoutput("sudo whoami"))) 
elif(("ifconfig" in cmd) or ("IP" in cmd) or ("ip" in cmd) or ("address" in cmd)):
  print(sp.getoutput("sudo ifconfig enp0s3"))
else:
  print("Try searching something else!")

