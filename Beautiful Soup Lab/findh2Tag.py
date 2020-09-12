from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.python.org')
soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.find_all('h2', limit=4)

for header in soup:
    print(header)
