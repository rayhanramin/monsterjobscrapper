import requests
import re
from bs4 import BeautifulSoup
import pprint

#a sample web link from the bugzilla website(A list of bugs for firefox is available in our github repo.)
URL = "https://bugzilla.mozilla.org/show_bug.cgi?id=1000185"

page = requests.get(URL)
#pprint.pprint(page.content)

if page.status_code != 200:
    print('Can not retrieve the requested url %s', URL)
    exit(1)

#parse the content of the webpage
soup = BeautifulSoup(page.content,'html.parser')

#separate the comments fromt the other html element
comments = soup.find_all('div', class_ ='change-set')

# find all the comments with activity tag
for i in comments:
    activity_tag = i.find('div',class_ ='activity')
    if activity_tag is None:
        continue
    else:
        pre_tag = i.find('pre', class_='comment-text')
        markdown_tag = i.find('div', class_ = 'comment-text markdown-body')
        changeset_tag = activity_tag.find_all('div', class_ = 'change')
        for j in changeset_tag:
            main_text = j.text.strip()
            pattern = re.compile("Resolution: --- → FIXED")
            if pattern.search(main_text):
                if markdown_tag is None:
                    links = pre_tag.find_all('a')
                    #print(pre)
                    for z in links:
                        print(z.text.strip())
                else:
                    new_links = markdown_tag.find_all('a')
                    for z in new_links:
                        print(z.text.strip())
