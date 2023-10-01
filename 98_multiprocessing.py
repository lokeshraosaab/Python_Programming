import multiprocessing
import concurrent.futures
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")
 
# for using parallel downloading or we can say multiprocessing 
# if we have internet speed of 100 GBPS and server can give us only 200 mbps then we can 
# perform multiprocessing for use our internet speed by giving more load to server in parallel

if __name__ == "__main__" :               # to get out of a error  
  url = "https://picsum.photos/200/300"
  # pros = []
  # for i in range(4):
  #   # downloadFile(url, i) # this is for downloading one by one
  #   p = multiprocessing.Process(target=downloadFile, args=[url, i])
  #   p.start()
  #   pros.append(p)

  # for p in pros:
  #   p.join()

  with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(6)]
    l2 = [i for i in range(6)]
    results = executor.map(downloadFile, l1, l2)
    for r in results:
      print(r)