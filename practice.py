#6

num=int(input('Enter a number: '))

if num % 2 ==0:
    print('Even number')
else:
    print('Odd number')

#7

for i in range(1,11):
     
    if i==5:
        continue
    if i==8:
        break
    print(i)  