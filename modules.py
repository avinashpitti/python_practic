 # what is class
# what is method
# How to access a method




x = 10
print(id(x))  # Address A

x = x + 1
print(id(x))  # Address B (A new address!)
import copy
li=[10,20,25]
shallow=copy.copy(li)
deep=copy.deepcopy(li)
print(li)
print(id(li))
print(id(shallow))

x='helloworld'
y='helloworld'

print(x is y)