import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
#pprint.pprint(page.content)

soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='SearchResults')
#print(results.prettify())

job_elements = results.find_all('section', class_ ='card-content')

for i in job_elements:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    job_title = i.find('h2', class_='title')
    company_name= i.find('div', class_='company')
    job_location = i.find('div', class_='location')
    if None in (job_title,company_name,job_location):
        continue
    print(job_title.text.strip())
    print(company_name.text.strip())
    print(job_location.text.strip())
    print()

