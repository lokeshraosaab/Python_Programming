import time
t = time.strftime('%H:%M:%S') 
# print(t)
hour = int(time.strftime('%H'))
name = (input("Enter name: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning, "+ name +"!")

elif(hour>=12 and hour<17):
  print("Good Afternoon Sir, "+ name +"!")
elif(hour>=17 and hour<24):
  print("Good Evening Sir, "+ name +"!")