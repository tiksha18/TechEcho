import webbrowser
import speech_recognition as sr
import pyttsx3
import os

pyttsx3.speak("Welcome")
pyttsx3.speak("Tell me,  how may I help you ")
r = sr.Recognizer()

while(True):

     with sr.Microphone() as source :
          print("Listening...")
          audio = r.listen(source)
          pyttsx3.speak("Okay, got it !")
          pyttsx3.speak("Now, Follow me")

          ch = r.recognize_google(audio)
          print (ch)

          if ((("start" in ch) or ("launch" in ch) or ("run" in ch) or ("show" in ch) or ("setup" in ch) or ("use" in ch) or ("open" in ch)) and (("linux" in ch) or ("Linux" in ch)) and (("service" in ch) or ("commands") or ("browser" in ch) or ("Browser" in ch))): 
               webbrowser.open("http://192.168.0.182/lrun.html")
               pyttsx3.speak("Opening linux browser")
          elif ((("know" in ch) or ("tell" in ch) or ("search" in ch)) and (("ip" in ch) or ("IP" in ch)) and (("address" in ch) or ("addresses" in ch))): 
               webbrowser.open("http://192.168.0.182/lrun2.html")
               pyttsx3.speak("You can take help from here")
          elif ((("start" in ch) or ("launch" in ch) or ("run" in ch) or ("show" in ch) or ("setup" in ch) or ("use" in ch) or ("open" in ch)) and (("docker" in ch) or ("Docker" in ch)) and (("service" in ch) or ("commands") or ("browser" in ch) or ("Browser" in ch))):
               webbrowser.open("http://192.168.0.182/drun3.html")
               pyttsx3.speak("Opening docker browser") 
          elif ((("start" in ch) or ("execute" in ch) or ("launch" in ch) or ("run" in ch) or ("open" in ch) or ("set up" in ch) or ("opening" in ch)) and ("docker" in ch) and (("os" in ch) or ("OS" in ch) or ("container" in ch))):
               webbrowser.open("http://192.168.0.182/drun2.html")
               pyttsx3.speak("Launch your Container from here by giving its name and image")
          elif ((("stop" in ch) or ("close" in ch) or ("restrict" in ch) or ("shut" in ch) or ("don't want" in ch)) and ("docker" in ch) and (("os" in ch) or ("OS" in ch) or ("container" in ch))):
               webbrowser.open("http://192.168.0.182/drun4.html")
               pyttsx3.speak("Stop a container from here by giving its name")
          elif (("exit" in ch) or ("quit" in ch) or ("stop" in ch) or ("get out" in ch) or ("close" in ch)):
               pyttsx3.speak("Thank you! Have  a nice day .")
               print("Good Bye !")
               break
          else:
               pyttsx3.speak("Unable to understand! Could you repeat please or try searching something else.")