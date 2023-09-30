# Exercise 10
# Use the NewsAPI and the requests module to fetch the daily news related to different topics.
#  Go to: https://newsapi.org/ and explore the various options to build you application

import requests
import json

query = input("What type of news are you interested in : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-08-30&sortBy=publishedAt&apiKey=20e36941da894afebc590e5773b9cca4"
response = requests.get(url)

# print(response.text)

news = json.loads(response.text)

# print(news,type(news))

for article in news["articles"] :
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------")