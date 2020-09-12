from bs4 import BeautifulSoup
import requests

page = requests.get('https://tekeye.uk/visual_studio/encrypt-decrypt-c-sharp-string')
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p')
print(soup.text)
