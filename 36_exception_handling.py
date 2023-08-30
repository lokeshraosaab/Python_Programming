# a = input("Enter the number : ")
# print(f"Multiplication table of {a} is : ")

# try:
#     for i in range(1,11):
#      print(f"{int(a)}X{i}= {int(a)*i}")
# # except:
# except Exception as e:
#     print(e)
#     print("Invalid Input")

# print("some important lines of code")
# print("end of the program")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3] # valid index are only 0,1
    print(a[num]) 
# we can handel different types of error by specifying under try :
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")
