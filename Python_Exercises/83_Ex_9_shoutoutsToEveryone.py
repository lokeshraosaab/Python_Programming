# Write a program to pronounce list of names using win32 API.
# If you are given a list l as follows:

# l = ["Rahul", "Nishant", "Harry"]

# Your program should pronouce:
# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

# Note: If you are not using windows, 
# try to figure out how to do the same thing using some other package

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
