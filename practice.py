# In positional arguments the output changes based on positions
def sub(a,b):
    return a-b
print(sub(6,3))
print(sub(3,6))



# Unlike positional arguments the output remains same in keyword arguemnts
def sub(a,b):
    return a-b
print(sub(a=6,b=3))
print(sub(b=3,a=6))

#Default arguments take default value if we don't provide the value

def add(a,b,c=10,d=14):
    return a+b+c+d

print(add(1,2,3,5))
print(add(1,2)) # It takes the default value only when if we don't provide
print(add(1,2,3))

#  Variable length arguments :
#It returns all the remaining values as a tuple

def cal(a,b,*c):
    return a,b,c

print(cal(1,2,3)) # c value is always return as a tuple even if it is single
print(cal(1,2,3,4,5,6)) # c value takes all the remaining values 
# print(cal(1)) # Typeerror
print(cal(1,2)) # Here c becomes an empty tuple





