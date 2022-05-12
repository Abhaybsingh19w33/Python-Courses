from bs4 import BeautifulSoup
import requests

url = 'www.facebook.com'
html_text = requests.get(url).txt
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

# only first job - find

jobs = soup.find_all('li' , çlass_='clearfix job-fix wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_ = "sim_posted").span.text

    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist_comp_name').text.strip()

        skills = job.find('span', class_ = 'srp-skills').text.strip()

        more_info = job.header.h2.a['href']
        print(f"Company Name: {company_name.strip()}")
        print(f"Required Skills: {skills.strip()}")
        print(f"More Info: {more_info}")

        # print(f'''
        # Company Name: {company_name}
        # Required Skills: {skills}
        # ''')

        print('')