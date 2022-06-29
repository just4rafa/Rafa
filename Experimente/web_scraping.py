from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://aternos.org/server/')
soup = BeautifulSoup(html_text.raw, 'lxml')

status = soup.find_all('div', id = 'start', class_ = 'btn btn-huge btn-success')
print(status)
