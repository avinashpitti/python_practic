def greet(name='guest'):
    print(f'hello {name}')
greet('Avinash')
greet()

def calculate(a,b):
    return a+b, a-b, a*b, a/b, a//b
result=calculate(17,4)
print(result)