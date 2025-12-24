# # print the given user input is a 3 digit number 

# num=int(input("Enter a number: "))

# if num >=100 and num < 1000:
#     print("It's a 3 digit number")
# else:
#     print("It's not a 3 digit number")



# #print the given user input is divisible by 6

# num=int(input("Enter your number: "))
# if num %6==0:
#     print("It is divisible by 6")
# else:
#     print("It's not divisible by 6")


# if "salaman":
#     print("Still Bachelor")
# else:
#     print("we dont know")

# enames=["RG","SG","PG","Modi"]

# for ename in enames:
#     print(ename)


# eids=(101,102,103,101,102,103)
# for eid in eids:
#     print(eid)

# uids={101,101,102,103,True}

# for uid in uids:
#     print(uid)

# employees=[
#     {'eid':101,'ename':'Rahul','gender':'M'},
#     {'eid':102,'ename':'Sonia','gender':'F'},
#     {'eid':103,'ename':'Priyanka','gender':'F'},
#     {'eid':104,'ename':'Modi','gender':'M'}
# ]

# for emp in employees:
#     print(emp['ename'])

# print first 10 even numbers

i=0
number=0 # 0 is an even number
limit =10

while i<limit:
    if number%2==0:
        print(number)
        i+=1
    number+=1



#print first 10 odd numbers
i=0
number=1 # Initial number
limit =10

while i<limit:
    if number%2==1:
        print(number)
        i+=1
    number+=1


number=int(input("Enter number of even number:"))

i=2
while i<=number*2:
    print(i,end=' ')
    i+=2




