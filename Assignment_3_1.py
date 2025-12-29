#1. Print numbers from 1 to 10 using a for loop?

for i in range(1,11):
    print(i)

print('********************')

#2. Print numbers from 1 to 10 using a while loop?

i=1

while i<=10:
    print(i)
    i+=1


print('********************')


#3. Program to calculate the sum of the first 10 natural numbers using for Loop and while loop?

sum=0
for i in range(1,11):
    sum+=i
print("sum of first 10 natural numbers:",sum)



sum=0
i=1

while i <=10:
    sum+=i
    i+=1
print('sum of first 10 natural numbers: ',sum)


#4. Program to print 15 to 10 numbers using for loop and while loop?

for i in range(15,9,-1):
    print(i)

print('**********for**********')

i=15

while i>=10:
    print(i)
    i-=1

print('*********while*********')


#5. Program to print 15 to 10 numbers using a while loop?

i=15

while i>=10:
    print(i)
    i-=1

print('*********while*********')


#6. Program to print the first 10 even numbers using a while loop?

count=0

num=2

while count < 10 :
    print(num)
    num+=2
    count+=1

print('********6 completed********')


#7. Program to print the first 5 even numbers using a for loop?

i=0
for i in range(1,6):
    print(i*2)

print('********7 completed********')



#8. Program to print the first 10 odd numbers using a while loop?

count=0

i=1

while count<10:
    print(i)
    count+=1
    i+=2

print('********8 completed********')

#9. Print Good Morning 10 times?

text="Good Morning"
for i in range(10):
    print(text)

print('********9 completed********')


#10.Print numbers from 10 to 1 descending order?

for i in range(10,0,-1):
    print(i)

print('********10 completed********')

#11.Print odd numbers from 10 to 30?

# for i in range(11,30,2):
#     print(i)

for i in range(10,31):
    if i%2!=0:
        print(i)

print('********11 completed********')

#12.Program to print the first 5 even numbers using a for loop?
for i in range(1,6):
    print(i*2)

print('********12 completed********')

#13.Program to print the first 5 odd numbers using a for loop?

for i in range(5):
    print(i*2+1)

print('********13 completed********')

#14.Program first ten multiples of 4 using a for loop(4,8,12,16...)?

for i in range(1,11):
    print(i*4)


#15.Program first ten multiples of 5 using a while loop(5,10,15,20...)?

i=1

while i <=10 :
    print(i*5)
    i+=1