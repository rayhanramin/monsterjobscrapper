import requests
import re
from bs4 import BeautifulSoup
import pprint

URL = "https://bugzilla.mozilla.org/show_bug.cgi?id=1504452"

page = requests.get(URL)
#pprint.pprint(page.content)

soup = BeautifulSoup(page.content,'html.parser')
comments = soup.find_all('div', class_ ='change-set')


for i in comments:
    print(i.text.strip())
