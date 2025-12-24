text="Helloworld"


for char in text[:5]:
    print(char,end=" ")
print()
    

print

employee={
    "id":101,
    "name":"avinash",
    "dept":"IT Services"
}

for emp in employee:
    print(emp)

for value in employee.values():
    print(value)

for key,value in employee.items():
    print(key,":",value)

print(employee["name"])
print(employee["id"])
print(employee["dept"])
