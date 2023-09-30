import requests
from bs4 import BeautifulSoup

# # requests.get("url")
# response = requests.get("https://www.codewithharry.com")
# print(response.text)

# #requests.post(url, headers = headers, json = data)
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }

# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }

# response = requests.post(url, headers=headers, json=data)
# print(response.text)


url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)