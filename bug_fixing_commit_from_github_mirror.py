'''
extract classes that cause vulnerabilities
'''

import re
import pandas as pd
from git import Repo
import multiprocessing as mp
import time
import csv

#df = pd.read_csv('C:\\Users\\aqd14\\Documents\\GitHub\\vulnerability-prediction\\firefox\data\\firefox.csv', sep=',')
#bug_ids = df['bug_id'].dropna().astype(int).sort_values(ascending = False).tolist()

repo_path = 'C:\\Users\\rohan\\gecko-dev'
repo = Repo(repo_path)


# d = {}


j=0
g = repo.iter_commits("master")
bug_fix = re.compile("^Bug.[0-9]{6,7} - Fix")

# with open('bugfixing_commits_rev_ids111.csv', 'r') as rf:
#     next(csv.reader(rf))
#     for i in csv.reader(rf):
#         git_sha = str(i[2].strip('\n'))
#         print(git_sha)
#         #exit(1)

csv_file = open('bugfixing_commits_git_hub.csv', 'w', newline ='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Bug_id', 'Fixing_commit_hash', 'commitdate'])


for commit in g:
    if bug_fix.search(commit.summary):
        #print(commit.summary)
        result = commit.summary.split(' ')
        bug_id = result[1]
        commitdate = time.strftime("%Y-%m-%d %H:%M:%S +0000", time.gmtime(commit.committed_date))
        sha = commit.hexsha
        csv_writer.writerow([bug_id,sha,commitdate])
    #print(commit.stats.files.keys())
    #print(commit.committed_date)
    #time.asctime(time.gmtime(commit.committed_date))
    #print(time.strftime("%Y-%m-%d %H:%M:%S +0000", time.gmtime(commit.committed_date)))


csv_file.close()
