import pymongo

from pymongo import MongoClient

from bs4 import BeautifulSoup

import requests

import datetime

import time

process = True

myClient = MongoClient()

db = myClient.my_currency_database

users = db.users

page = requests.get("https://www.exchangerates.org.uk/Pounds-to-Rupees-currency-conversion-page.html")

soup = BeautifulSoup(page.content, "html.parser")

conversion_rates = soup.find(id="conversion-chart-today")

conversion_data = conversion_rates.find(class_="convtop").get_text()

content = conversion_data[0:]

print(content)

times = datetime.datetime.now()

print(times)

while process == True:
    times = datetime.datetime.now()

    user1 = ({"GBP to INR": content, "Date and Time": times})

    user_id = users.insert_one(user1).inserted_id

    time.sleep(43200)
