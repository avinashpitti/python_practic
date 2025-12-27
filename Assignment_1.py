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
    print(f"All employees : {employee["ename"]}")

print("---------1 done-----------")

#2. print employee names whose age is greater than 50

for employee in employees:
    if employee["age"] > 50 :
        print(f"Employees whose age >50: {employee["ename"]}")

print("---------2 done-----------")

#3. Count total number of Male employees

Male_count=0

for employee in employees:
    if employee['gender']=="Male":
        Male_count+=1
print(f'total number of Male employees is {Male_count}')

print("---------3 done-----------")


#4. Count total number of Female employees

Female_count=0

for employee in employees:
    if employee['gender']=="Female":
        Female_count+=1
print(f'total number of Female employees is {Female_count}')

print("--------4 done------------")


#5. print employees whose age is exactly 59

for employee in employees:
    if employee["age"]==59:
        print(employee["ename"])

print("----------5 done----------")


#6. print employee names whose age is less than 40

for employee in employees:
    if employee["age"]<40:
        print(employee["ename"])

print("---------6 done-----------")


#7. print employee names whose age is between 30 and 50

for employee in employees:
    if employee["age"]>30 and employee["age"]<50:
        print(employee["ename"])

print("---------7 done-----------")


#8. Print employee name and age if the employee is Female.

for employee in employees:
    if employee["gender"]=='Female':
        print(employee["ename"],employee["age"])
        
print("--------8 done------------")


#9. Print employee name and age if the employee is Male.

for employee in employees:
    if employee['gender']=="Male":
        print(employee["ename"],employee["age"])

print("---------9 done-----------")

#10. Print employees whose name starts with the letter “A”.

for employee in employees:
    if employee["ename"].startswith("A"):
        print(employee["ename"])


print("--------10 done------------")


#11. For each employee, print “Senior Employee” if age ≥ 60 else “Regular Employee”

for employee in employees:
    if employee["age"] >=60:
        print("Senior Employee")
    else:
        print('Regular Employee')

print("---------11 done-----------")



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

print("----------12 done----------")


#13. Print employees eligible for retirement (age ≥ 60).

for employee in employees:
    if employee["age"]>=60:
        print(employee["ename"])

print("--------13 done------------")

#14. Check if there is any employee above 80 years and print their name.

for employee in employees:
    if employee["age"]>80:
        print(employee["ename"])


print("--------14 done------------")

#15. Print employee name with label “Actor” if Male else “Actress”.

for employee in employees:
    if employee["gender"] == "Male":
        label = "Actor"
    elif employee["gender"] == "Female":
        label = "Actress"
    else:
        label = "Performer"

    print(f'{employee["ename"]} is an {label}')

print("--------15 done------------")


#16. Print employees whose age is an even number.

for employee in employees:
    if employee["age"]%2==0:
        print(employee["ename"])

print("--------16 done------------")



#17. Print employees whose age is an odd number.

for employee in employees:
    if employee["age"]%2!=0:
        print(employee["ename"])

print("--------17 done------------")


#18. Print employees with eid divisible by 5.

for employee in employees:
    if employee['eid']%5==0:
        print(f'eid divisible by 5 : {employee["ename"]}')

print("--------18 done------------")


#19. Print employees whose name length is greater than 12 characters.

for employee in employees:
    if len(employee["ename"])>12:
        print(f'ename whose character lenght is >12: {employee["ename"]}')

print("--------19 done------------")


#20. Print employees whose age ends with digit 7 or 9.

for employee in employees:
    if str(employee["age"]).endswith(("7", "9")):
        print(employee["ename"])


#professional pythonic way:

# for employee in employees:
#     if employee["age"] % 10 in (7, 9):
#         print(employee["ename"])


print("--------20 done------------")


#21. Stop printing employees once you find an employee aged 82 (break).

for employee in employees:
    if employee["age"]==82:
        break
    print(employee["ename"])

print("--------21 done------------")

#22. Skip printing employees whose gender is Female (continue).

for employee in employees:
    if employee["gender"]=='Female':
        continue
    print(employee["ename"])

print("--------22 done------------")


#23. Skip employees whose age < 40, print the rest.

# When the question says “skip”, think continue, not pass.

for employee in employees:
    if employee["age"] < 40 :
        continue
    else:
        print(employee["ename"])

print("--------23 done------------")

#24. Print employees until you encounter eid = 10, then stop.

for employee in employees:
    if employee["eid"]==10:
        break
    print(employee["ename"])

print("--------24 done------------")


#25. Print only first 5 employees using a loop and break.

count=0

for employee in employees:
    print(employee['ename'])
    count+=1
    if count==5:
        break

print("--------25 done------------")

#26. Skip employees whose name contains the word “Khan”.

for employee in employees:
    if 'Khan' in employee["ename"]:
        continue
    else:
        print(employee["ename"])


print("--------26 done------------")



#27. Print employees until you find a Female employee above 50.

for employee in employees:
    if employee["gender"]=='Female' and employee["age"] > 50 :
        break
    print(employee['ename'])


print("--------27 done------------")


#28. Print employees except those whose eid is even.

for employee in employees:
    if employee["eid"]%2==0:
        continue
    print(employee["ename"])


print("--------28 done------------")

#29. Print employee names but stop once Rajinikanth is found.

for employee in employees:
    if employee["ename"]=='Rajinikanth':
        break
    print(employee["ename"])

print("--------29 done------------")

#30. Skip printing employees whose age is greater than 70.

for employee in employees:
    if employee["age"]>70:
        continue
    print(employee["ename"])

print("--------30 done------------")


#31. Print Male employees above 50 and Female employees above 45.

for employee in employees:
    if (employee['gender']=='Male' and employee["age"]>50) or \
    (employee["gender"]=='Female' and employee["age"]>45):
        print(employee["ename"])

print("--------31 done------------")


#32. Print employees grouped as:
# ● Male Senior
# ● Female Senior
# ● Male Non-Senior
# ● Female Non-Senior

for employee in employees:
    if (employee["gender"]=="Male" and employee["age"]>=60 ):
        print(f'Male senior {employee["ename"]}')
    elif (employee["gender"]=="Female" and employee["age"]>=60 ):
        print(f'Female senior{employee["ename"]}')
    elif (employee["gender"]=="Male" and employee["age"]<60):
        print(f'Male Non-senior {employee["ename"] }')
    elif (employee["gender"]=='Female' and employee["age"]<60):
        print(f'Female Non-senior {employee["ename"]}')

print("--------32 done------------")

#33. Print employees whose age is prime.

for employee in employees:
    age=employee["age"]
    if age > 1 :
        for i in range(2, int(age**0.5)+1):
            if age% i ==0 :
                break

        else:
            print(f'{employee["ename"]} (age :{age})')

print("--------33 done------------")

#34. Print employees whose age is a multiple of 3 and 5.

for employee in employees:
    if employee["age"]%3==0 and employee["age"]%5==0 :
        print(employee["ename"])
# A number divisible by both 3 and 5 is divisible by 15. you may try with 15 instead of 3 and 5

print("--------34 done------------")

#35. Print employee names in uppercase if age ≥ 50 else lowercase.

for employee in employees:
    if employee["age"]>=50:
        print(employee["ename"].upper())
    else:
        print(employee["ename"].lower())


print("--------35 done------------")


#36. Print employees whose eid and age are both even.

for employee in employees:
    if employee["eid"]%2==0 and employee["age"]%2==0:
        print(employee["ename"])

print("--------36 done------------")

#37. Print employees whose eid is odd and age > 40.

for employee in employees:
    if employee["eid"]%2==1 and employee["age"] > 40 :
        print(employee["ename"])

print("--------37 done------------")

#38. Print employees who are Male and age between 45–60.

for employee in employees:
    # if (employee["gender"]=='Male') and (employee["age"] >= 45 and employee["age"] <=60 ) :
    if (employee["gender"]=='Male') and 45 <= employee['age'] <=60 :
        print(employee["ename"])

print("--------38 done------------")


#39. Print employees who are Female and age less than 40.

for employee in employees:
    if( employee["gender"]=='Female') and employee["age"] < 40 :
        print(employee["ename"])

print("--------39 done------------")

#40. Print employees and mark them as:
# ● "Veteran" → age ≥ 70
# ● "Experienced" → age 50–69
# ● "Rising Star" → age < 50

for employee in employees:
    if employee["age"] >= 70:
        print(f'{employee["ename"]} is a veteran ')
    elif 50 <= employee["age"] <= 69 :
        print(f'{employee["ename"]} is an experienced ')
    elif employee["age"] < 50 :
        print(f'{employee["ename"]} is a Rising star ')

# Method 2 :

# for employee in employees:
#     age = employee["age"]

#     if age >= 70:
#         label = "Veteran"
#     elif 50 <= age <= 69:
#         label = "Experienced"
#     else:
#         label = "Rising Star"

#     print(f'{employee["ename"]} is a {label}')


print("--------40 done------------")


print("--------END------------")


    
      
