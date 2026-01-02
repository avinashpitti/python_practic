# import random

# print(random.randint(1,100)) 

# print(random.random())

# import datetime

# now=datetime.datetime.now()

# print("present date and time ", now)

# print("year",now.year)
# print("month",now.month)
# print("date",now.day)
# print('hour',now.hour)
# print('minute',now.minute)
# print('second',now.second)

# today=datetime.date.today()
# print(today)

# d=datetime.date(2023,5,12)
# print(d)

# #1️⃣ Even or Odd

# num=int(input("Enter a number: "))

# if num %2==0:
#     print(f'{num} is an even number')
# else:
#     print(f'{num} is an odd number.')

# # 2️⃣ Positive, Negative or Zero

# num=int(input("Enter a number: "))
# if num>=1:
#     print(f'{num} is a positive number')
# elif num==0:
#     print(f'{num} is neither positive nor negative.')
# else:
#     print(f'{num} is a negative number.')

# # 3️⃣ Count Vowels in a String

# para='I am learning python fullstack development.'

# count=0

# for ch in para.lower():
#     if ch in ('a','e','i','o','u'):
#         count+=1
# print(count)

# length=print(len(para))

# rev=''
# for ch in para:
#     rev=ch+rev

# print(rev)


# # Take input from the user and reverse it using loop

# name=input("Enter your name: ")
# rev=''
# for ch in name:
#     rev=ch+rev
# print(f'Your name is {name}')
# print(f'Your reversed name is {rev}')


# Find the largest number in a list without using max()

nums=[3,6,78,12,35,99,1]

largest=nums[0]

for num in nums:
    if num > largest:
        largest=num
print(largest)

# count frequency of elements:
nums= [1, 2, 2, 3, 1, 4, 2]

# reverse a string

subject='python'
rev=''

for ch in subject:
    rev = ch+rev
print(rev)