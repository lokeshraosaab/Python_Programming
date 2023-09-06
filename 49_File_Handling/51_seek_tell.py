with open('file.txt', 'r') as f:
    print(type(f))
  # Move to the 10th byte in the file
    f.seek(10)
  # Read the next 5 bytes
    print(f.read(5))
    print("\n")
    print("As we are using with as so the file will be close just after executed last instruction under this")

with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  print(f.read(10))  

  # Save the current position
  current_position = f.tell()
  print(current_position)

  # Seek to the saved position
  # f.seek(current_position) #if we seek current position or not next time read(x) will read next x bytes from
  # those characters that are already read
  print(f.read(2))
  print("\n")

with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('sample.txt', 'r') as f:
  print(f.read())