import  csv
import re


csv_file = open('bugfixing_commits_git_hub_firefox.csv', 'w', newline ='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Bug_id', 'creationdate', 'resolutiondate', 'hash', 'commitdate'])


file1 = open("bugfixing_commits_git_hub.csv")
n1 = list(csv.DictReader(file1))
file2 = open("opening_closing_bug_dates1.csv")
n2 = list(csv.DictReader(file2))


# Bug_id	Fixing_commit_hash	commitdate
# Bug_id	creationdate	resolutiondate



for i in n1:
    for j in n2:
        if i['Bug_id']==j['Bug_id']:
            a = i['Bug_id'].strip('\n')
            b = j['creationdate'].strip('\n')
            c = j['resolutiondate'].strip('\n')
            d = i['Fixing_commit_hash'].strip('\n')
            e = i['commitdate'].strip('\n')
            print(a,b,c,d,e)
            csv_writer.writerow([a,b,c,d,e])
            break


csv_file.close()
file1.close()
file2.close()
