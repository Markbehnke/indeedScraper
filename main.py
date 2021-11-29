import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class main:

    def extract(page):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        # grabs the url and page number. Note: page 2 = start=10. Page 1 = start = 0
        url = f'https://ca.indeed.com/jobs?q=software%20developer%2C%20programmer&l=Canada&start={page}'
        r = requests.get(url, headers)

        soup = BeautifulSoup(r.content, 'html.parser')
        return soup

    def transform(soup):
        divs = soup.find_all('div', class_='job_seen_beacon')
        for item in divs:
            # Finds all the titles of the job descriptions
            title = item.find('h2').text.strip()
            # Remove the "new" word
            title = title.replace("new", "")
            # Finds company names
            company = item.find('span', class_='companyName').text.strip()
            # Finds salary
            try:
                salary = item.find('div', class_='salary-snippet').text.strip()
            except:
                salary = ''

            print(title)

        return

# jobsearch-jobDescriptionText

    def transformJob(soup):
        divs = soup.find(
            'div', attrs={"class": 'jobsearch-jobDescriptionText'}).findAll('li')
        for item in divs:
            try:
                desc = item.text.strip()
                print(desc)
            except:
                continue

    c = extract(0)
    transform(c)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    # grabs the url and page number. Note: page 2 = start=10. Page 1 = start = 0
    url = f'https://ca.indeed.com/jobs?q=software%20developer%2C%20programmer&l=Canada&start=10'
    r = requests.get(url, headers)

    # Begin looping through all detailed job descriptions on a page
    soup = BeautifulSoup(r.content, 'html.parser')
    allLinks = []

    for link in soup.findAll('a', {'target': '_blank'}):
        if 'js=3' in link.get('href'):
            allLinks.append(link.get('href'))

    # Create 2nd soup object for every job page to use for parsing
    for link in allLinks:
        jobURL = 'https://ca.indeed.com' + link
        jobResponse = requests.get(jobURL)
        jobData = jobResponse.content
        jobSoup = BeautifulSoup(jobData, 'html.parser')
        transformJob(jobSoup)
