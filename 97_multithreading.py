import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)
  return seconds

def main():
    # # Normal Code
    # time1 = time.time()
    # func(4) 
    # func(2)
    # func(1)
    # time2 = time.time()
    # print(time2 - time1)

    # Same code using Threads
    time3 = time.time() 
    # function call ko thread ka use krke reserve krke rkhna
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    # background m start kr dene ke liye turnt hi
    t1.start()
    t2.start()
    t3.start()
    # task ke khtm hone ke wait krne ke liye
    t1.join()
    t2.join()
    t3.join()
    # calculating time
    time4 = time.time()
    print(time4 - time3)

def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func, 3)
    # future2 = executor.submit(func, 2)
    # future3 = executor.submit(func, 4)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)


poolingDemo()

