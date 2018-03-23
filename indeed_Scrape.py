import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://www.indeed.com/jobs?q=fintech&l=New+York"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")
#printing soup in a more structured tree format that makes for easier reading
# print(soup.prettify())

allData = []
jobs = []
city = []
company = []
def extract_job_title_from_result(soup):
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        # jobDetails = ''
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])
            # jobDetails = a["title"] + '****'
        c = div.find_all("span", attrs={"class": "location"})
        for span in c:
          city.append(span.text)
        #   jobDetails += span.text + '*****'
        comps = div.findAll("span", attrs={"class": "company"})
        for a in comps:
            print(a.text)
            print(type(a.text))
            company.append(a.text)
        # allData.append(jobDetails)
extract_job_title_from_result(soup)

# print(jobs)
# print(allData)
# print(soup.find_all(name="div", attrs={"class":"row"}))
