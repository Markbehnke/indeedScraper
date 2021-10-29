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

    url = getURL('software developer', 'Canada')

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Get job titles
    cards = soup.find_all(
        'h2', class_='jobTitle jobTitle-color-purple jobTitle-newJob')

    # Prototype the model with a single record:
    card = cards[0].div

    print(card['span'])
