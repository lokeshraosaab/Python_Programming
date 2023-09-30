import shutil
import os

# shutil.copy("87_shutil_module.py", "87_shutil_module2.py")
# shutil.copy2("87_shutil_module.py", "87_shutil_module2.py")
# shutil.copytree("cluttered", "mycluttered")
# shutil.move("cluttered/a.txt", "a.txt")
# shutil.rmtree("mycluttered")
# os.remove("a.txt")
# os.remove("87_shutil_module2.py")



# shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. 
# If the destination location already exists, the original file will be overwritten.

# shutil.copy2(src, dst): This function is similar to shutil.copy,
# but it also preserves more metadata about the original file,
# such as the timestamp.

# shutil.copytree(src, dst): This function recursively copies the directory located at src 
# to a new location specified by dst. If the destination location already exists,
# the original directory will be merged with it.

# shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. 
# This function is equivalent to renaming a file in most cases.

# shutil.rmtree(path): This function recursively deletes the directory located at path, 
# along with all of its contents. 
# This function is similar to using the rm -rf command in a shell.

# os.remove("filename") : as there is no command in shutil to remove a file so it used to remove a file
# using import os
