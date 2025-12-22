#arithmetic operators works with integers,floats,complex and boolean values only

a=7
b=4
c=True
d=False


print("The value of a+b is",a+b)
print("The value of a-b is",a-b)

print("The value of a*b is",a*b)
print("The value of a/b is",a/b)

print("The value of a//b is",a//b)
print("The value of a**b is",a**b)
print("The value of a%b is",a%b)

print("The value of a+c is",a+c)
print("The value of b+d is",b+d)

print("The value of a**d is",a**d)
print("The value of a**c is",a**c)

e=3+8j

print("The value of d+e is",d+e)
print("The value of c+e is",c+e)

f="avinash "

# print("The product of a*f is",(f+' ')*a)



print("The product of f* a is",(f*a).strip())

print(True/True)
# print(True/False) # zero division error

print(False/True)


print(0.1+0.2)

quotient,remainder=divmod(18,4)
print("quotient",quotient)
print("remainder",remainder)



