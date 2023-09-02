marks = [12, 56, 32, 98, 12,  45, 1, 4]

# i = 0
# for mark in marks:
#   print(mark)
#   if(i == 3):
#     print("Harry, awesome!")
#   i +=1

# for i, mark in enumerate(marks):
for i, mark in enumerate(marks, start = 1):
  print(mark)
  if(i == 3):
    print("Harry, awesome!")