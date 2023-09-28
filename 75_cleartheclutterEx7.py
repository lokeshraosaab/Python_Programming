import os

files = os.listdir("cluttered")
i = 1
for file in files:
    if file.endswith(".webp"):
     print(file)
     os.rename(f"cluttered/{file}" , f"cluttered/{i}.webp")
     i = i+1

# os.rename("cluttered/file.txt","cluttered/a.txt")
