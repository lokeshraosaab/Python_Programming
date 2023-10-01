import argparse
import requests

def download_file(url, local_filename): 
  if local_filename is None:
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
  with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              # If you have chunk encoded response uncomment if
              # and set chunk_size parameter to None.
              #if chunk: 
              f.write(chunk)
  return local_filename

parser = argparse.ArgumentParser()

# Add Command Line Arguements

# parser.add_argument("arg1", help = "description of arg1")
# parser.add_argument("arg2", help = "description of arg2")
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", help="Name of the file", default=None)

# Parse the arguements
args = parser.parse_args()

# Use the arguments in your code
# print(args.arg1)
# print(args.arg2)

print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)

# iss program ko run krne ke line command line pr yhi == "python filename url" and then enter.