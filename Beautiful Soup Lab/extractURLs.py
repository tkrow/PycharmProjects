from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.python.org')
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('li')

for link in soup.find_all('a', href=True):
    print(link['href'])
