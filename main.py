"""
DataBase will probably contain the following:
ID: (Given)
Course Section and Number:
Course Name:
Course Description:
Credits:
Prerequisite:

Nested Dic{ 'CS 110' : {'course_name': 'Introduction to Internet Programming and Applications', 'credits': '3', 'prerequisite': {'none': none, 'none': none}}
"""

from majorscrape import scrape_specific, scrape

print(scrape_specific())  # Scraping catered for CS HONORS Students
print(scrape())  # Scraping CCSU CS Smartcatalog website
