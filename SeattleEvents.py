from bs4 import BeautifulSoup
import bs4
import requests
import csv
"""
Created 2/9/2020
This program scrapes the Stranger website for Seattle events then
stores data in to a csv

Columns of the csv = ['eventNames', 'categories', 'eventDates', 'venues', 'neighborhoods', 'prices']

NOTE: Number of Dates are inconsistent with how many events availabe. Needs revision.
"""
url = "https://www.thestranger.com/events/?page=5"
# Temp data storage for one neighborhood
neighborhood_desc = []
# request for data from the server using GET
r = requests.get(url)
# turn the data into text and use beautiful soup to parse data
data = r.text
soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify())

eventNames = []
categories = []
eventDates = []
venues = []
neighborhoods = []
prices = []

count = 0
for header in soup.find_all('h3'):
     #print(header.get_text())
     if count > 1:
        name =  header.get_text().strip().split('\n')[0]
        eventNames.append(name)
        category = header.get_text().strip().split('\n')[-1]
        categories.append(category)
     count += 1
print(len(eventNames), eventNames)
print(len(categories), categories)


count = 0
for p_tag in soup.find_all('p', {'class', "event-row-date"}):
    #print(count)
    if count > 0:
        #print(p_tag.get_text().strip())
        eventDates.append(p_tag.get_text().strip())
    count += 1
print(len(eventDates), eventDates)

count = 0
for p_tag in soup.find_all('span', {'class', "event-row-venue"}):
    #print(count)
    if count % 2 == 0:
        #print(p_tag.get_text().strip())
        venues.append(p_tag.get_text().strip())
    count += 1
print(len(venues), venues)

count = 0
for p_tag in soup.find_all('span', {'class', "event-row-neighborhood"}):
    print(count)
    if count % 2 == 0:
        print(p_tag.get_text().strip())
        neighborhoods.append(p_tag.get_text().strip())
    count += 1
print(len(neighborhoods), neighborhoods)

count = 0
for p_tag in soup.find_all('span', {'class', "event-row-event-price"}):
    print(count)
    print(p_tag.get_text().strip())
    prices.append(p_tag.get_text().strip())
    count += 1
print(len(prices), prices)



# # create the csv file
# with open('SeattleEvents.csv', mode='w') as csv_file:
#     fieldnames = ['eventNames', 'categories', 'eventDates', 'venues', 'neighborhoods', 'prices']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for desc in neighborhoods:
#         writer.writerow({'neighborhood': desc[0],
#                          'description': desc[1],
#                          'history': desc[2],
#                          'vibe': desc[4],
#                          'activities_attractions': desc[5]})
#
