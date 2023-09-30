# importing the pyttsx library
import pyttsx3
import time # for using time.sleep(x)

# initialisation
engine = pyttsx3.init()

# testing
engine.say("My first code on text-to-speech")

engine.runAndWait() # to run the speech we use runAndWait() 

# Shoutouts to given names in the lists

names = ["Lokesh Rao Sahab", "Shivam Rao Sahab", "Shivam Tyagi", "Ankit Bhai", "Kadambdi Nikhil", "Aman Tyagi"]

for name in names :
    engine.say(f"Shoutout to {name}")

engine.runAndWait()

time.sleep(2)
engine.say("Thanks for using this")
engine.runAndWait()
