# def calc(a,b):
#     return a+b
# calc(10) #TypeError: calc() missing 1 required positional argument: 'b'

a=100
def login():
    print("login success")

print(type(login()))
print(type(a))
login()
# logout() # NameError: name 'logout' is not defined


def add():
    print("Addition")
add() # It returns Addition
# add(10) # TypeError: add() takes 0 positional arguments but 1 was given


def add(a,b):
    print(a+b)
add(10,20)
# add(10,'20')TypeError: unsupported operand type(s) for +: 'int' and 'str'
# add('10',20)TypeError: can only concatenate str (not "int") to str
add('10','20') # 1020



# Types of arguments

# positional arguments: order matters(values go by positon)
def subtract(a, b):
    return a - b

print(subtract(10, 5))   # 5
print(subtract(5, 10))   # -5

# keyword arguments: order doesn't matter
def subtract(a, b):
    return a - b

print(subtract(a=10,b=5))   # 5
print(subtract(b=5,a=10))   # 5

# Defualt arguments

def cal(a,b,c=100):
   print(a+b+c) 

cal(1,2,3)
cal(1,2)
# cal(1)TypeError: cal() missing 1 required positional argument: 'b'
# cal(1,2,3,4)TypeError: cal() takes from 2 to 3 positional arguments but 4 were given

# variable length arguments(*args)

def cal(a,b,*c):
    print(a,b,c)
cal(2,3,4)
cal(2,3,4,5)
cal(2,3,4,5,6)
cal(2,3,4,5,6,7,8)


# keyword variable length arguments(**args)

def user_details(**info):
    for key, value in info.items():
        print(key, ":", value)
user_details(name="Avinash", age=22, city="Bangalore")

def calc(a,b):
    return a+b,'hello'
result=calc(10,20)

print(result)

print("*****************************")


def outer():
    print('outer function starts')

    def inner():
        print('Inner function')

    inner()
    inner()
    inner()

outer()
outer()

print("*****************************")


def outer():
    print('outer function started')

    def inner():
        print("inner function")
    
    return inner

outer()()

print("*****************************")

def outer():
    print('outer function started')

    def inner():
        print("inner function")
    
    return inner

x=outer()
x()
x()

print("*****************************")




