import requests
import re
from bs4 import BeautifulSoup
import pprint

#a sample web link from the bugzilla website(A list of bugs for firefox is available in our github repo.)
URL = "https://bugzilla.mozilla.org/show_bug.cgi?id=1444506"

page = requests.get(URL)
#pprint.pprint(page.content)

if page.status_code != 200:
    print('Can not retrieve the requested url %s', URL)
    exit(1)

soup = BeautifulSoup(page.content,'html.parser')

#separate the comments fromt the other html element
comments = soup.find_all('div', class_ ='change-set')

for i in comments:
    chng = i.find('div',class_ ='activity')

    if chng is None:
        continue
    else:
        pre = i.find('pre', class_='comment-text')
        changeset = chng.find_all('div', class_ = 'change')
        for j in changeset:
            ser = j.text.strip()
            pat = re.compile("Resolution: --- → FIXED")
            if pat.search(ser):
                links = pre.find_all('a')
                #print(pre)
                for z in links:
                    print(z.text.strip())