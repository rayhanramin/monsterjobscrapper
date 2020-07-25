'''
extract classes that cause vulnerabilities
'''

import re
import pandas as pd
from git import Repo
import multiprocessing as mp
import time

#df = pd.read_csv('C:\\Users\\aqd14\\Documents\\GitHub\\vulnerability-prediction\\firefox\data\\firefox.csv', sep=',')
#bug_ids = df['bug_id'].dropna().astype(int).sort_values(ascending = False).tolist()

repo_path = 'C:\\Users\\rohan\\gecko-dev'
repo = Repo(repo_path)


# d = {}

ids = []
files = []
commit_hashes = []
committers = []
i=0
g = repo.iter_commits("master")
bug_fix = re.compile("^Bug.[0-9]{6,7} - Fix")

for commit in g:
    if bug_fix.search(commit.summary):
        #print(commit.committed_date)
        #time.asctime(time.gmtime(commit.committed_date))
        print(time.strftime("%Y-%m-%d %H:%M:%S +0000", time.gmtime(commit.committed_date)))
        i+=1

print(i)
