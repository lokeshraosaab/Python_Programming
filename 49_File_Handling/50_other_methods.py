# f = open('myfile3.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline() #The readline() method reads a single line from the file with a \n in the end of the line
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)
# f.close()

# lines = f.readlines() #The readlines() method reads all the lines of the file and returns them as a list of strings.
# print(lines) # Output: ['56,45,67\n', '12,34,63\n', '13,64,23\n']


f = open('myfile4.txt', 'w')
lines = ['line-1\n', 'line-2\n', 'line-3\n']
f.writelines(lines)
f.close()