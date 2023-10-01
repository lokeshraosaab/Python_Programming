# Exercise 11 - Drink Water Reminder
# Write a python program which reminds you of drinking water every hour or two. 
# Your program can either beep or send desktop notifications for a specific operating system

import time
import pyttsx3
from plyer import notification


engine = pyttsx3.init()
Reminder_time = float(input("tell the time after which you will drink water : "))
while(True):
    time.sleep(Reminder_time)
    engine.say("You Should Drink Water")
    notification.notify(title = "Notification",
                        message = "You should drink water",
                        timeout = 5)
    engine.runAndWait()