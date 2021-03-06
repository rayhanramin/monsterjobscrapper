import requests
import re
from bs4 import BeautifulSoup
import csv
import time

csv_file = open('bugfixing_commits1.csv', 'w', newline ='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Bug_id', 'Fixing_commit_url'])

# base url for bugzilla
URL = "https://bugzilla.mozilla.org/show_bug.cgi?id="

# open file for reading the bug ids for mozilla firefox
with open('firefox-bug_ids.txt','r') as re_file:
    for bug_ids in re_file:
        bug_ids = bug_ids.strip('\n')
        new_url = URL + str(bug_ids)
        #print(new_url)
        time.sleep(5)
        page = requests.get(new_url)
        # pprint.pprint(page.content)

        if page.status_code != 200:
            print('Can not retrieve the requested url %s', URL)
            exit(1)

        # parse the content of the webpage
        soup = BeautifulSoup(page.content, 'html.parser')

        # separate the comments fromt the other html element
        comments = soup.find_all('div', class_='change-set')
        if comments is None:
            continue
        else:
            for i in comments:
                activity_tag = i.find('div', class_='activity')
                if activity_tag is None:
                    continue
                else:
                    pre_tag = i.find('pre', class_='comment-text')
                    markdown_tag = i.find('div', class_='comment-text markdown-body')
                    changeset_tag = activity_tag.find_all('div', class_='change')
                    for j in changeset_tag:
                        main_text = j.text.strip()
                        pattern = re.compile("Resolution: --- → FIXED")
                        if pattern.search(main_text):
                            if pre_tag:
                                links = pre_tag.find_all('a')
                                # print(pre)
                                for z in links:
                                    fixing_link = z.text.strip()
                                    print(bug_ids, fixing_link)
                                    csv_writer.writerow([bug_ids, fixing_link])
                            elif markdown_tag:
                                new_links = markdown_tag.find_all('a')
                                for z in new_links:
                                    fixing_link_n = z.text.strip()
                                    print(bug_ids, fixing_link_n)
                                    csv_writer.writerow([bug_ids,fixing_link_n])
                        else:
                            continue

re_file.close()

csv_file.close()