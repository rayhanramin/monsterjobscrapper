import csv
import re
...


pat = re.compile("mozilla-central", re.IGNORECASE)

with open('bugfixing_commits2.csv','r') as in_file:
    with open('bugfixing_commits1.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if pat.search(row[1]):
                writer.writerow(row)
out_file.close()
in_file.close()



