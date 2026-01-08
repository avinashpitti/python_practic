def func(name='kumar'):
    print(name)
func('avinash')
func('narasimha')
func()

func('naveeen')



def fun(animal,name):
    print("I have a ",animal)
    print('my',animal+" 's name is ",name)

fun(animal='dog',name='puppy')
fun(animal='cat', name='cheeku')


x=lambda a:a+4
print(x(47))

def add(x,y):
    return x+y
print(add(5,6))

add = lambda x,y : x+y

print(add(3,5))


print('************************')

num=[10,20,30,40]

print(list(map(lambda num:num+1,num)))


from datetime import datetime
from datetime import date
employees=[
    {"eid":101,"ename":"Rahul"},
    {"eid":102,"ename":"Sonia"},
    {"eid":103,"ename":"Priya"},
    {"eid":104,"ename":"Modi"},
]
#for every employee obj add new key:value 
# loc:"Banglaore"
def addnewpropery(emp):
    emp['loc']='Bangalore'
    emp['created']=datetime.now().isoformat()
    return emp 

emp_map_obj=map(addnewpropery,employees)
new_employees=list(emp_map_obj)
print(new_employees)