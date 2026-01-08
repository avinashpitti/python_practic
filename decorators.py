def say_hello():
    print("Hello!")

def execute(func):
    func()


def outer():
    def inner():
        print('Inner function executed')

    return inner

result=outer()
result()