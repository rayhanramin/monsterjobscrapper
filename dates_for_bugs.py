from bs4 import BeautifulSoup
import re
import csv
import requests
import time

csv_file = open('opening_closing_bug_dates.csv', 'w', newline ='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Bug_id', 'creationdate','resolutiondate'])

url = "https://bugzilla.mozilla.org/show_bug.cgi?id="

with open('bugfixing_commits1.csv','r') as in_file:
    for i in csv.reader(in_file):
        URL = url + str(i[0].strip('\n'))
        print(URL)
        time.sleep(5)
        page = requests.get(URL)

        if page.status_code != 200:
            print('Can not retrieve the requested url %s', URL)
            time.sleep(600)
            continue

        soup = BeautifulSoup(page.content,'html.parser')