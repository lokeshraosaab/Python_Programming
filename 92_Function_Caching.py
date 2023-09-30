from functools import lru_cache
import time

# Memoization is an optimization technique used to speed up computer programs 
# by caching the results of expensive function calls and returning ..

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5
    
init = time.time()
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
t0 = time.time() - init
print(t0)

# jis bhi value ke liye dobara calc kreinge uske liye turant aa jayega cache memory se uthakr de dega
init = time.time()
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
t1 = time.time() - init
print(t1)

# Here we are creating init and t2 to find time taken
init = time.time()
print(fx(61)) # iske liye calc hi krna pdega bcz repeat nhi hua h to time lgega or cache m save bhi ho jayega
t2 = time.time() - init
print("done for 61")
print(t2)

# or cache memory program end hote hi destroy bhi ho jaati h so it is not bad to use @lru_cache(maxsize = ?)