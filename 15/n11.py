import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class": "column"})

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldPrice = li.find("div", {"class": "proDetail"}).find_all("span")[0].text.strip().strip("TL")
    newPrice = li.find("div", {"class": "proDetail"}).find_all("span")[1].text.strip().strip("TL")
    print(f"name: {name} link: {link} old price: {oldPrice} new price: {newPrice}")
