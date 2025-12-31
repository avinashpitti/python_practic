import random

print(random.randint(1,100)) 

print(random.random())

import datetime

now=datetime.datetime.now()

print("present date and time ", now)

print("year",now.year)
print("month",now.month)
print("date",now.day)
print('hour',now.hour)
print('minute',now.minute)
print('second',now.second)

today=datetime.date.today()
print(today)

d=datetime.date(2023,5,12)
print(d)