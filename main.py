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

print("Welcome to the Currency Converter!")

while True:

    inputs_choice = input("What would you like to convert?\n1.Pounds\n2.Dollars\n3.Rupees\n4.Australian Dollars\n5.Euros\n")

    list = ["Pounds", "Dollars", "Rupees", "Australian-Dollars", "Euros"]

    new_list = list[int(inputs_choice) - 1]

    option = input("What would you like to convert " + new_list + " with?\n")

    now_list = list[int(option) - 1]

    page = requests.get("https://www.exchangerates.org.uk/" + new_list + "-to-" + now_list + "-currency-conversion-page.html")

    soup = BeautifulSoup(page.content, "html.parser")

    conversion_rates = soup.find(id="conversion-chart-today")

    conversion_data = conversion_rates.find(class_="convtop").get_text()

    content = conversion_data[0:]

    print(content)

    times = datetime.datetime.now()

    print(times)

    times = datetime.datetime.now()

    user1 = ({"GBP to INR": content, "Date and Time": times})

    user_id = users.insert_one(user1).inserted_id

