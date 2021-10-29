import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class main:

    def getURL(position, location):
        # The curly braces indicate the job search and location
        template = 'https://ca.indeed.com/jobs?q={}&l={}'
        url = template.format(position, location)
        return url

    url = getURL('software developr', 'Canada')

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
