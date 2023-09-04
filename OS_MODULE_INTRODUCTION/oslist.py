import os 
folders = os.listdir("data")

print(os.getcwd())
# os.chdir("/Users")
# os.chdir("/Users/yaduv/OneDrive/Desktop/Python_Programming/OS_MODULE_INTRODUCTION")
# print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))