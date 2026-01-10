#1

name='avinash'
age=22
height=1.56
student=True

print(name,age,height,student)

#2

a=10
b=3

sum=a+b
difference=a-b
multiplication=a*b
division=a/b
remainder=a%b

print(sum)
print(difference)
print(multiplication)
print(division)
print(remainder)

#3

fruits=['orange','banana','apple','guava','papaya']

print(fruits[0])
print(fruits[-1])
fruits.append('kiwi')
print(fruits)
fruits.remove('banana')
print(fruits)

#4

numbers=(1,2,3)

nums=set(numbers)

print(f'nums before adding a number : {nums}')

nums.add(4)
print(f'nums after adding a number : {nums}')

my_details={
    'name':'Avinash',
    'age': 22,
    'course':'python'
}

print(f"my course : {my_details['course']}")

my_details['age']=23

print(f'my updated age : {my_details['age']}')

my_details['city']='bangalore'

print(my_details)