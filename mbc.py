import os
import requests
from bs4 import BeautifulSoup

query = "안세영"
search_url = "https://search.imbc.com/news?qt={query}"

download_folder = f"./{query}"

response = requests.get(search_url)
soup = BeautifulSoup(response.text,"html.parser")

image_tage = soup.find("ul", class_= "list-type news-list")
lis = image_tage.find_all("ul")

for img_tah in lis:
    img_url = image_tag.find("img").get("src")
    img_data = requests.get(f"https{img_url}").content
    