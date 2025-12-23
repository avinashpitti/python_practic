if "salman":
    print("bachelor")
else:
    print("He is not a bacherlor")

enames=['sg','pg','rg','modi']
for ename in enames:
    print(ename)


eids=(101,102,103,101,102,103)
for eid in eids:
    print(eid)


uids={101,101,102,103}
for uid in uids:
    print(uid)

employees=[
    {'eid':101,'ename':'rahul','gender':'male'},
    {'eid':102,'ename':'sonia','gender':'female'},
    {'eid':103,'ename':'priya','gender':'female'}


]

for emp in employees:
    print(emp["ename"])

#1. Take an input from user and check whether it's a 3 digit number or not
num=int(input("Enter a number:"))

if num >= 100 and num < 1000:
    print("It's a 3 digit number")
else:
    print("It's not a 3 digit number")
print(type(num))