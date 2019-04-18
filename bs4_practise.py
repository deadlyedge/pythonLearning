from bs4 import BeautifulSoup
import requests

data = requests.get('https://www.google.com').content

soup = BeautifulSoup(data, 'html.parser')
#
# links =soup.findAll('a')
# for link in links:
#     print(link)

print(soup.body.div.attrs)
