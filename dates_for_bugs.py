from bs4 import BeautifulSoup
import re
import csv
import requests
import time

csv_file = open('opening_closing_bug_dates1.csv', 'w', newline ='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Bug_id', 'creationdate','resolutiondate'])

url = "https://bugzilla.mozilla.org/show_bug.cgi?id="

with open('new_firefox_bugs.txt','r') as in_file:
    #next(csv.reader(in_file))
    for i in in_file:
        bug_ids = i.strip('\n')
        URL = url + bug_ids
        print(URL)
        #exit(1)
        time.sleep(5)
        page = requests.get(URL)

        if page.status_code != 200:
            print('Can not retrieve the requested url %s', URL)
            time.sleep(600)
            continue

        soup = BeautifulSoup(page.content,'html.parser')
        span = soup.find('span', id = 'field-value-status_summary')
        if span is None:
            continue

        dates = span.find_all('span', class_ = 'rel-time')
        if None in dates:
            continue

        op_date = time.strftime("%Y-%m-%d %H:%M:%S +0000",time.gmtime(int(dates[0].get('data-time'))))
        cl_date = time.strftime("%Y-%m-%d %H:%M:%S +0000",time.gmtime(int(dates[1].get('data-time'))))
        print(op_date)
        print(cl_date)
        csv_writer.writerow([bug_ids, op_date,cl_date])

in_file.close()
csv_file.close()