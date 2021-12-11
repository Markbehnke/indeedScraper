import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import time


class main:

    def extract(page, jobTitle):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        # grabs the url and page number. Note: page 2 = start=10. Page 1 = start = 0
        url = f'https://ca.indeed.com/jobs?q={jobTitle}&l=Canada&start={page}'
        r = requests.get(url, headers)

        soup = BeautifulSoup(r.content, 'html.parser')
        return soup


# jobsearch-jobDescriptionText


    def transformJob(soup, jobNum):
        desc = ""
        try:
            divs = soup.find(
                'div', attrs={"class": 'jobsearch-jobDescriptionText'}).findAll('li')
            for item in divs:
                desc += f"{item.text.strip()} "
        except:
            pass
        with open('programmer.txt', 'a', encoding="utf-8") as outfile:
            outfile.write(f'ScrapedJobID{jobNum}:\n{desc}\n')

    jobNum = 1
    page = 0
    # Change this variable for which job you are searching by
    jobTitle = "programmer"
    # Currently 100 pages of jobs.
    while(page <= 1000):
        print("Currently on page", page / 10)
        time.sleep(11)
        c = extract(page, jobTitle)

        # Begin looping through all detailed job descriptions on a page
        soup = extract(page, jobTitle)
        allLinks = []

        for link in soup.findAll('a', {'target': '_blank'}):
            if 'js=3' in link.get('href'):
                allLinks.append(link.get('href'))

        # Create 2nd soup object for every job page to use for parsing
        for link in allLinks:
            time.sleep(11)
            jobURL = 'https://ca.indeed.com' + link
            jobResponse = requests.get(jobURL)
            print("Scraping", jobURL)
            jobData = jobResponse.content
            jobSoup = BeautifulSoup(jobData, 'html.parser')
            transformJob(jobSoup, jobNum)
            jobNum += 1
        # page number. Note: page 0 = first page, page 10 = second page, page 20 = third page etc.
        page += 10
    # Make your file then change this to the output
