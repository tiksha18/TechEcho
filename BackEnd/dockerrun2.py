#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
cmd = form.getvalue("t")

if(("docker" in cmd) and ("version" in cmd)):
  print(sp.getoutput("sudo docker --version"))
elif((("current status" in cmd) or ("status" in cmd) or ("active" in cmd)) and ("docker" in cmd)):
  print("Current Status of Docker :")
  print(sp.getoutput("sudo systemctl status docker"))
elif(("information" in cmd) and ("docker" in cmd)):
  print("Docker Information :")
  print(sp.getoutput("sudo docker info"))
elif((("container" in cmd) or ("os" in cmd)) and ("running" in cmd)):
  print("All the current O.S./Container running inside Docker are :")
  print(sp.getoutput("sudo docker ps"))
elif(("docker" in cmd) and ("images" in cmd)):
  print("All Docker Images :")
  print(sp.getoutput("sudo docker images"))
elif(("docker" in cmd) and ("commands" in cmd)):
  print("Docker Commands :")
  print(sp.getoutput("sudo docker --help"))
else:
  print("Try something else!")

