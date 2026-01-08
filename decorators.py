def greet():
    print('hello')
x=greet
x()

def greeting():
    return 'hello,guys'
x=greeting
print(x())



def outer():
    text_outer = 'This is an outer function.'
    
    def inner():
        return 'This is an inner function.'
    
    text_inner = inner()
    return text_outer, text_inner # Returning two values

y, z = outer() # Unpacking the two values
print(y)
print(z)

def say_hello():
    print("Hello!")

def execute(func):
    func()

execute(say_hello)
