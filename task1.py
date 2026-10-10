import requests


print("Hello Scrapper!")

url = "https://example.com"

response = requests.get(url)

print(response.text)