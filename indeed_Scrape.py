import requests
import bs4
from bs4 import BeautifulSoup
import csv

#This is the list that will hold the dictionary for each job
listOfDict = []

#URL to scrape data from
URL = "https://www.indeed.com/jobs?q=fintech&&start=%d"
# page = requests.get(URL)
# soup = BeautifulSoup(page.text, "html.parser")
#To print the soup in a more structured format
#print(soup.prettify())



#This function extracts Job data from a webpage
def extract_job_title_from_result(soup):
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        # Initiate empty object to hold data for a job
        jobDict = {}

        # Fetch Job Title
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobDict["jobTitle"] = a["title"]

        # Fetch Job Location
        c = div.find_all("span", attrs={"class": "location"})
        for span in c:
          jobDict["location"] = span.text

        # Fetch Company name
        comps = div.findAll("span", attrs={"class": "company"})
        for a in comps:
            compStr = ''
            compStr = a.text.replace(" ", "")
            compStr = compStr.replace("\n", "")
            jobDict["company"] = compStr

        #Append this job to our list of jobs
        listOfDict.append(jobDict)


# X is our counter
# newURL is each new URL to scrape
x = 0
newURL = ''
while x < 991:
    newURL = URL % (x)
    print(newURL)
    #Fetch the page from the internet
    page = requests.get(newURL)

    #Parse the HTML
    soup = BeautifulSoup(page.text, "html.parser")

    #Extract all the relevant job details
    extract_job_title_from_result(soup)

    #Increment X to move to next page
    x += 10

#Extract headers to put in as column names in our excel
keys = listOfDict[0].keys()

#Write each job entry to the excel file
with open('jobCount.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(listOfDict)
