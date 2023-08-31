a = int(input("Enter the value between 5 and 9 : "))

if a<5 or a>9 :
    raise ValueError("Value should be between 5 and 9")

# Quick Quiz

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
#   # code...