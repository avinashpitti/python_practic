employees = [
{"eid": 1, "ename": "Shah Rukh Khan", "gender": "Male", "age": 59},
{"eid": 2, "ename": "Deepika Padukone", "gender": "Female", "age": 38},
{"eid": 3, "ename": "Amitabh Bachchan", "gender": "Male", "age": 82},
{"eid": 4, "ename": "Priyanka Chopra", "gender": "Female", "age": 42},
{"eid": 5, "ename": "Aamir Khan", "gender": "Male", "age": 59},
{"eid": 6, "ename": "Kareena Kapoor", "gender": "Female", "age": 44},
{"eid": 7, "ename": "Salman Khan", "gender": "Male", "age": 59},
{"eid": 8, "ename": "Katrina Kaif", "gender": "Female", "age": 41},
{"eid": 9, "ename": "Hrithik Roshan", "gender": "Male", "age": 50},
{"eid": 10, "ename": "Alia Bhatt", "gender": "Female", "age": 31},
{"eid": 11, "ename": "Akshay Kumar", "gender": "Male", "age": 57},
{"eid": 12, "ename": "Kangana Ranaut", "gender": "Female", "age": 37},
{"eid": 13, "ename": "Ranbir Kapoor", "gender": "Male", "age": 42},
{"eid": 14, "ename": "Vidya Balan", "gender": "Female", "age": 46},
{"eid": 15, "ename": "Ranveer Singh", "gender": "Male", "age": 39},
{"eid": 16, "ename": "Anushka Sharma", "gender": "Female", "age": 36},
{"eid": 17, "ename": "Rajinikanth", "gender": "Male", "age": 74},
{"eid": 18, "ename": "Aishwarya Rai", "gender": "Female", "age": 51},
{"eid": 19, "ename": "Vijay", "gender": "Male", "age": 50},
{"eid": 20, "ename": "Madhuri Dixit", "gender": "Female", "age": 57}
]


#1.print all employee names using for loop

for employee in employees:
    print(employee["ename"])

print("--------------------")

#2. print employee names whose age is greater than 50

for employee in employees:
    if employee["age"] > 50 :
        print(employee["ename"])

print("--------------------")

#3. Count total number of Male employees

Male_count=0

for employee in employees:
    if employee['gender']=="Male":
        Male_count+=1
print(f'total number of Male employees is {Male_count}')

print("--------------------")


#4. Count total number of Female employees

Female_count=0

for employee in employees:
    if employee['gender']=="Female":
        Female_count+=1
print(f'total number of Female employees is {Female_count}')

print("--------------------")


#5. print employees whose age is exactly 59

for employee in employees:
    if employee["age"]==59:
        print(employee["ename"])

print("--------------------")


#6. print employee names whose age is less than 40

for employee in employees:
    if employee["age"]<40:
        print(employee["ename"])

print("--------------------")


#7. print employee names whose age is between 30 and 50

for employee in employees:
    if employee["age"]>30 and employee["age"]<50:
        print(employee["ename"])

print("--------------------")


#8. Print employee name and age if the employee is Female.

for employee in employees:
    if employee["gender"]=='Female':
        print(employee["ename"],employee["age"])
        
print("--------------------")


#9. Print employee name and age if the employee is Male.

for employee in employees:
    if employee['gender']=="Male":
        print(employee["ename"],employee["age"])

print("--------------------")

#10. Print employees whose name starts with the letter “A”.

for employee in employees:
    if employee["ename"].startswith("A"):
        print(employee["ename"])


print("--------------------")


#11. For each employee, print “Senior Employee” if age ≥ 60 else “Regular Employee”

for employee in employees:
    if employee["age"] >=60:
        print("Senior Employee")
    else:
        print('Regular Employee')

print("--------------------")



#12. Print “Young”, “Middle-aged”, or “Senior” based on age:
# ● <40 → Young
# ● 40–59 → Middle-aged
# ● >=60 → Senior

for employee in employees:
    if employee['age']<40:
        print(f'{employee["ename"]} is young')
    elif employee["age"]>=40 and employee["age"]<60:
        print(f'{employee["ename"]} is Middle-aged')
    else:
        print(f'{employee["ename"]} is Senior')

print("--------------------")


#13. Print employees eligible for retirement (age ≥ 60).

for employee in employees:
    if employee["age"]>=60:
        print(employee["ename"])

print("--------------------")

#14. Check if there is any employee above 80 years and print their name.

for employee in employees:
    if employee["age"]>80:
        print(employee["ename"])


print("--------------------")

#15. Print employee name with label “Actor” if Male else “Actress”.





