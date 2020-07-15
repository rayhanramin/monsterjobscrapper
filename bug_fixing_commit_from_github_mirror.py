'''
extract classes that cause vulnerabilities
'''

import re
import pandas as pd
from git import Repo
import multiprocessing as mp

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
g = repo.iter_commits("master", max_count=10000)
bug_fix = re.compile("Fix")

for commit in g:
    if bug_fix.search(commit.summary):
        print(commit.summary)
        i+=1
        if(i==100):
            break


