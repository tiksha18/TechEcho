#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
cmd = form.getvalue("i")

if("Google" in cmd):
  print(sp.getoutput("sudo nslookup www.google.com"))
elif("YouTube" in cmd):
  print(sp.getoutput("sudo nslookup www.youtube.com"))
elif("Microsoft" in cmd):
  print(sp.getoutput("sudo nslookup www.microsoft.com"))
elif("Amazon" in cmd):
  print(sp.getoutput("sudo nslookup www.amazon.com"))
elif("Gmail" in cmd):
  print(sp.getoutput("sudo nslookup www.gmail.com")) 
elif("Yahoo" in cmd):
  print(sp.getoutput("sudo nslookup www.yahoo.com")) 
elif("Facebook" in cmd):
  print(sp.getoutput("sudo nslookup www.facebook.com")) 
elif("LinkedIn" in cmd):
  print(sp.getoutput("sudo nslookup www.linkedin.com")) 
elif("Flipkart" in cmd):
  print(sp.getoutput("sudo nslookup www.flipkart.com")) 
elif("Instagram" in cmd):
  print(sp.getoutput("sudo nslookup www.Instagram.com")) 
elif("Twitter" in cmd):
  print(sp.getoutput("sudo nslookup www.twitter.com")) 
elif("Whatsapp" in cmd):
  print(sp.getoutput("sudo nslookup www.whatsapp.com")) 
elif("Telegram" in cmd):
  print(sp.getoutput("sudo nslookup www.telegram.com")) 
elif("Discord" in cmd):
  print(sp.getoutput("sudo nslookup www.discord.com")) 
else:
  print("Try searching something else!")

