# even or odd


def even_odd(num):
    if num%2==0:
        print('even')
    else:
        print('odd')

even_odd(21)
even_odd(28)
even_odd(0)
even_odd(-34)
even_odd(-43)

print('******************')

def evenodd(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'
print(evenodd(22))
print(evenodd(33))
print(evenodd(-12))
print(evenodd(-34))
print(evenodd(0))


print('******************')

#prime

def is_prime(n):
    if n > 1 :
        for i in range(2,int(n**0.5)+1):
            if n % i ==0:
                print('Not a prime')
                break
        else:
            print('prime')
    else:
        print('Not a prime')
is_prime(21)
is_prime(23)
is_prime(31)





