# a = int(input("What is the time now "))
# if(a>=3 and a<=12):
#     print("Good Morning sir")
# elif(a>12 and a<=17):
#     print("Good Afternoon Sir")
# elif(a>17 and a<=23):
#     print("Good Evening Sir")
# else:
#     print("Good Night Sir")
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime