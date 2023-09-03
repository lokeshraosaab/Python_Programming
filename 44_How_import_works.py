# import pandas
# pandas.read_csv()

# import math
# a = math.floor(2.344456789)
# print(a)
# result = math.sqrt(9)
# print(result)

# from math import pi, sqrt
# result = sqrt(9)*pi
# print(result)

# It's also possible to import all functions and variables from a module using the * wildcard.
#  However, this is generally not recommended as it can lead to confusion and make it harder

# from math import *
# result = sqrt(9)
# print(result)  # Output: 3.0
# print(pi)  # Output: 3.141592653589793

# import math as m
# result = m.sqrt(9)
# print(result)  # Output: 3.0
# print(m.pi)  # Output: 3.141592653589793

# from math import pi, sqrt as s
# result = s(9)*pi
# print(result)

import math
print(dir(math))
print(math.nan, type(math.nan))





