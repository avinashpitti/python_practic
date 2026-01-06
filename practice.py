def outer():
    def inner():
        print("This is an inner function")
    inner()
outer()

print('************************')

def outer():
    name="Avinash"
    print(name)
    def inner():
        print(f"hello {name}")
    inner()
outer()

print('************************')


def outer():
    name='amar'
    
    def inner():
        print(f'hello {name}')

    inner()
outer()

print('************************')

def outer():
    x=10
    print(x)
    def inner():
        print(x+12)
    inner()
outer()

print('************************')

def outer():
    x=5
    def inner():
        return x+4
    return inner
func=outer()
print(func())
