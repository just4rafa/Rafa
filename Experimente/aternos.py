

from bs4 import BeautifulSoup, SoupStrainer
from requests import request
import requests


url = "https://aternos.org/server/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

span = soup.find(id= "fas fa-stop-circle")
stat = span.find(class_ = "statuslabel-label")
sttat =stat.find(class_ = "statuslabel-label")

print(sttat.text)