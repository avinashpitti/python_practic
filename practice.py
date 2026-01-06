def outer():
    print("outer functon")

    def inner():
        print("inner function")
    inner()
outer()

print('**************************')

def outer(name):
    print('outer function', name)

    def inner(name):
        print('inner function', name)
    inner('avinash')
outer('avinash')

print('**************************')


def outer():
    print('outer function')

    def inner(name):
        print('inner function', name)
    inner('avinash')
outer()

print('**************************')

def outer(name):
    print("outer function",name)

    def inner():
        print("inner function")
    inner()
outer('avinash')

