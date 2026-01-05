#1.Variable basics
Name="Avinash"

Age=22

Height= 5.2

student=True

std=15

print(f'Name : {Name}')
print(f'Age : {Age}')
print(f'Height : {Height}')
print(f'student : {student}')
print('std :',std)
print(f'std : {std}')

print(type(Name))

print(type(Age))

print(type(Height))

print(type(student))

#2.Typechecking
x = 10
y = 10.5
z = "Python"
a = True

print(f'data type of {x} is { type(x)}')
print(f'data type of {y} is {type(y)}')
print(f'data type of {z} is {type(z)}')
print(f'data type of {a} is {type(a)}')

#3.Multiple assignment
a,b,c=5,10,15
print(f'sum of numbers is : {a+b+c}')

#4.List

info=['Avinash',22,'Python']
print(info)
print(info[1])
info[2]='Python Full Stack'

print(info)

#5.Tuple

my_info=('Avi',23,5.2,True,'Bangalore')
print(my_info)
print(my_info[0][0])
print(my_info[-1][-1])

# my_info[2]=8 #TypeError: 'tuple' object does not support item assignment

#Bonus question

# The main difference between a list and a tuple is mutable and immutable respectively.

print("********** Level 1 done **********")

#6.set practice

nums = [1, 2, 2, 3, 4, 4, 5]

nums=set([1, 2, 2, 3, 4, 4, 5])
print(type(nums))

print(nums)

nums.add(6)

nums.remove(2) # nums.remove gives error if not present

#nums.discard(2) # No error

print(nums)

# Duplicates are removed automatically

#7. Dictionary

Avi_info={
    'name' : "Avinash",
    'age' : 22,
    'course' : 'Python',
    'city' : 'Bengaluru'
}

print(Avi_info)

print(Avi_info['course'])
Avi_info['city']='Hyderabad'
print(Avi_info)

Avi_info['email']='avinash123@gmail.com'
print(Avi_info)

#8. operators +conditionals

num=-45

if num > 0 :
    print('positive')
elif num==0 :
    print('zero')
else : 
    print('Negative')

print('*********** level 2 completed *************')

#9. for loops print numbers from 1 to 10

for i in range(1,11):
    print(i)

#10. Find the sum of numbers from 1 to 100 using a loop
n=100
sum=0

for i in range(1,n+1):
    
    sum+=i
print(f'The sum of numbers from 1 to 100 is {sum}')

#11. print only even numbers from 11 to 20

evens=[]
for i in range(11,21):
    if i % 2 ==0:
        # evens.append(i)
        evens.append(str(i))
# print(f'The even numbers from 11 to 20 is {evens}')
print(" ".join(evens))

#12. Print numbers from 10 to 1 using a while loop.

i=10

while i >= 1:
    print(i)
    i-=1

# Bonus

# break : is used to stop the iteration
# continue : is used to skip the current iteration

#11. I need all the values in the single line.
