from bs4 import BeautifulSoup
import requests

url = input("Enter the website name: ")

response = requests.get('http://' + url)
data = response.content

soup = BeautifulSoup(data, 'html5lib')

for link in soup.find_all('a'):
    try:
        if not link.get("href").startswith("http"):
            link = 'https://' + url + link.get("href")
        else:
            link = link.get("href")
        print(link)
    except Exception as e:
        continue
