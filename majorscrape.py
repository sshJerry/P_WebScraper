import re
import time
import urllib.request

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
isHonorsMain = ['CS 151', 'CS 152', 'CS 253', 'CS 254', 'CS 354', 'CS 355', 'CS 385', 'CS 463', 'CS 464', 'CS 483',
                'CS 492', 'CS 407', 'CS 415', 'CS 416', 'CS 418', 'CS 419', 'CS 423', 'CS 425', 'CS 455', 'CS 460',
                'CS 462', 'CS 465', 'CS 473', 'CS 481', 'CS 490', 'CS 491', 'CS 493', 'CS 495']


def web_request(page):
    try:
        req = urllib.request.Request(page, headers=headers)
        urlReq = urllib.request.urlopen(req)
        pageSoup = BeautifulSoup(urlReq, "lxml")
        return pageSoup
    except Exception as e:
        return str(e)


def parser():
    page = "https://ccsu.smartcatalogiq.com/current/Undergraduate-Graduate-Catalog/All-Courses/CS-Computer-Science"
    pageS = web_request(page)
    if pageS == 'HTTP Error 404: Not Found':
        return None
    else:
        contains = pageS.find("ul", {"class": "sc-course-list"})
        courseLinkList = []
        for listItems in contains.find_all("li"):
            courseLinkList.append("https://ccsu.smartcatalogiq.com" + listItems.find('a').get('href'))
        return list(dict.fromkeys(courseLinkList))


# Original method sourcing all information on smart catalog cs
def scrape():
    courses = parser()
    courseID = 0
    for course in courses:
        information = web_request(course)
        all_info = information.find("div", {'id': 'main'})
        courseSandNum = all_info.find('h1').find('span').string
        courseName = str(all_info.find('h1').contents[2]).strip()
        courseDescription = all_info.find('div', {'class': 'desc'}).get_text(strip=True)

        """ If wanting to uncomment, add  prerequisite and courseCredit to return or print
        x = re.findall(">3<", str(all_info.find('div', {'id': 'credits'})))  # Line 40
        if x:
            courseCredit = '3'
        else:
            courseCredit = "Literally Danger"
        prerequisite = {}
        if all_info.find('a', {'class': 'sc-courselink'}) is None:
            prerequisite[courseSandNum] = 'None'
        else:
            prerequisite[courseSandNum] = str(all_info.find('a', {'class': 'sc-courselink'}).text)
        """

        print(str(courseID) + "\n" + courseSandNum + "\n" + str(courseName) + "\n" + str(
            courseDescription) + "\n==========")
        courseID += 1
        time.sleep(2)


# Parsing for information solely in the CCSU CS HONORS tab
def scrape_specific():
    courses = parser()
    courseID = 0
    for course in courses:
        information = web_request(course)
        all_info = information.find("div", {'id': 'main'})
        courseSandNum = all_info.find('h1').find('span').string
        if courseSandNum in isHonorsMain:
            courseName = str(all_info.find('h1').contents[2]).strip()
            courseDescription = all_info.find('div', {'class': 'desc'}).get_text(strip=True)

            """ If wanting to uncomment, add  prerequistie and courseCredit to return or print
            x = re.findall(">3<", str(all_info.find('div', {'id': 'credits'})))
            if x:
                courseCredit = '3'
            else:
                courseCredit = "Literally Danger"
            """

            print(str(courseID) + "\n" + courseSandNum + "\n" + str(courseName) + "\n" + str(
                courseDescription) + "\n==========")
            courseID += 1
            time.sleep(1)
