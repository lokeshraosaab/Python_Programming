for i in range(12):
    if(i==10):
        break
    print("5 X ", i+1,"=", 5*(i+1))
print("loop se exit kr gya")

# break ka mtlb loop ko chhodkr nikl jaao
# continue ka mtlb iteration ko chhodkr nikl jaao

for i in range(12):
    if(i==10):
     print("Skip the iteration")
     continue
    print("5 X ", i,"=", 5*(i))

print("Emulation of do while loop in python")
i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break    

        
