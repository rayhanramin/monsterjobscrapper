from bs4 import BeautifulSoup
import re
import csv
import requests
import time

csv_file = open('bugfixing_commits_rev_ids11.csv', 'w', newline ='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Bug_id', 'Fixing_commit'])

with open('bug_fixing22.csv','r') as in_file:
    for i in csv.reader(in_file):
        URL = i[1].strip()
        bug_id = i[0]
        print(URL)
        time.sleep(5)
        page = requests.get(URL)

        if page.status_code != 200:
            print('Can not retrieve the requested url %s', URL)
            time.sleep(600)
            continue

        soup = BeautifulSoup(page.content,'html.parser')
        tbody = soup.find('div', class_ = 'title_text')
        if tbody is None:
            continue
        else:
            tr = tbody.find_all('tr')
            pat = re.compile("changeset")
            if None in tr:
                continue
            else:
                for i in tr:
                    td = i.find_all('td')
                    for j in td:
                        text = j.text.strip()
                        if pat.search(text):
                            rev = j.find_next_sibling('td').text.strip()
                            print(rev)
                            csv_writer.writerow([bug_id,rev])
                        else:
                            continue




in_file.close()
csv_file.close()