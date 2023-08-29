dic = {
    13 : "Lokesh",
    26 : "Rao Sahab",
    458 : "Shivam",
    789 : "Aman"
}

# print(dic[13])
# print(dic[26])
# print(dic[458])
# print(dic[789])

print(dic)

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info['name'])
print(info.get('name'))
# print(info['name2']) # throw error as name2 is not present in dictionary
print(info.get('name2')) # but .get returns none for the same
print(info.keys())
print(info.values())
print(info.items())

for key in info.keys():
    print(key)
    print(info[key])

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

for value in info.values():
    print(value)

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")