# write a program to check whether a number is even or odd
# method 1
n=int(input('Enter a number : '))

if n % 2 ==0 :
    print(f'{n} is an even number')
else:
    print(f'{n} is an odd number')

#method 2
n=int(input('Enter a number : '))
def odd_even(n):
    if n % 2 ==0 :
        return f"{n} is an even number"
    else :
        return f"{n} is an odd number"
print(odd_even(n))

#method 3
n=int(input('Enter a number : '))
def odd_even(n):
    return 'even' if n % 2==0 else 'odd'
print(f'{n} is {odd_even(n)}')

#method 4
n=int(input('Enter a number: '))
def odd_even(n):
    if n % 2 ==0 :
        print(f'{n} is an even number')
    else :
        print(f'{n} is an odd number')
odd_even(n)


# Find the sum of all numbers from 1 to n. 
#method 1 :
n=int(input('Enter a number : '))

def sum_nums(n):
    return n*(n+1)//2
total=sum_nums(n)
print(total)

#method 2 :
n=int(input('Enter a number :'))
def sum_nums(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
print(sum_nums(n))

