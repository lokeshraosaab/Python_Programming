ep1 = {122: 45, 123: 89, 567: "Aman", "Hello": 69}
ep2 = {222: 67, 566: 90}

print(ep1)
ep1.update(ep2)
print(ep1)
print(ep2)

ep1.pop(122)
print(ep1)

ep1.popitem() # remove last key value pair
print(ep1)

# del ep1  # delete the entire dictionary as key is not provided to the del keyword and it returns name error
del ep1[123]
print(ep1)

ep1.clear()
print(ep1)
