import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.select("span.text")
author = soup.select("small.author")

quotes_data = []
author_data = []

for i in quotes:
    quotes_data.append(i.text)

for i in author:
    author_data.append(i.text)

#print(author data)
data = {
    "Author": author_data,
    "Quotes": quotes_data
}

df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)