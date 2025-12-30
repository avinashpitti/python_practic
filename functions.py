def greet():
    print("Hello, Avinash")
greet()


def greeting(user):
    print("Hey", user)

greeting('Amar')


def addi(a,b):
    print(a+b)
addi(23,34)
addi(78,90)

def add(a,b):
    return a+b

result=add(2,5)
print(result)

def demo1():
    print(10)

def demo2():
    return 10

x=demo1()
y=demo2()

print(x)
print(y)

# num=int(input("Enter a number: "))
def evn_odd(num):
    if num %2==0:
        return "even"
    else:
        return "odd"
# print(evn_odd(num))
print(evn_odd(45))
print(evn_odd(34))

#f_to_c
def f_to_c(f):
    return (f-32)*5/9
print(f_to_c(56))
print(f_to_c(57))
print(f_to_c(59))


# c_to_f

def c_to_f(c):
    return (c*1.8)+32
print(c_to_f(40))
print(c_to_f(47))
print(c_to_f(43))


def empty_function():
    pass


def square(n):
    return n*n
def cube(n):
    return square(n)*n
print(cube(6))



#Buit-in functions

nums=[10,20,30]        
print(f'length of function: {len(nums)}')
print(f' sum of function:{sum(nums)}')
print(f'max value of function: {max(nums)} ')
print(f' min value of function: {min(nums)}')
print(f' type of function: {type(nums)}')


# User-defined functions

def mul(a,b):
    return a*b
result=mul(14,18)
print(f'multiplication of 2 numbers is: {result}')

# Arguments

# positional arguments:order matters

def subtract(a,b):
    return a-b
res=subtract(23,12)
res1=subtract(12,21)
print(f'The subtract of 2 values is {res}')
print(f'The subtract of 2 values is {res1}')

# keyword arguments : order does not matter

def greet(name,age):
    print(name,age)

greet("Avinash",20)
greet(age=22,name='Amar')


# Default Arguments

def login(user='Guest'):
    print('welcome',user)

login()
login("Admin")

# variable length arguments
# without *args

def add(a,b,c):
    return a+b+c
print(add(2,3,6))

# def add(a,b,c):
#     return a+b+c
# print(add(2,3,6,7)) #takes 3 arguments but 4 were given



# with *args: you can give any number of arguments.

def add(*nums):
    total=0
    for num in nums:
        total+=num
    return total

print(add(10,23,21))
print(add(3,5))
print(add(6,3,9,8,2,45,78,65))


# Keyword variable length arguments(**kwargs): used when values come as key-value pairs

def user_details(**info):
    for key,value in info.items():
        print(key,':',value)

print(user_details(name='avinash',city='bangalore',gender='Male'))
print(user_details(name='chandu',city='hyderabad'))


# return multiple values from function

def operations(a,b):
    return a+b,a-b,a*b,a/b
w,x,y,z=operations(10,5)
print(w,x,y,z)


#Local vs Global variable

x=100 # global

def demo():
    x=50    # local
    print(x)
demo()
print(x)#Local variable has priority inside function


# Global keyword

x = 10

def change():
    global x
    x = 70

change()
print(x)

#prime_check

def is_prime(n):
    if n <= 1 :
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

print(is_prime(5))
print(is_prime(51))

x=lambda a :a+7
print(x(4))

y= lambda b : b*4
print(y(5))

z= lambda c : c-4
print(z(32))


def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(7)
print(mydoubler(5))





















