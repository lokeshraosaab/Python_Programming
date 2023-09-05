# Reading a file

f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# Writing to a file

f = open('myfile2.txt', 'w')
# f = open('myfile2.txt', 'a')
f.write(' Hello , World!')
f.close()

# Alternatively,we can use the with statement to automatically close the file after we are done with it.
with open('myfile2.txt', 'a') as f:
  f.write(" Hey I am inside with")