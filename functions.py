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
