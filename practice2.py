names=['avinash','varun','rakesh','amar','chandu',3,['samson','gill','abhishek','ishan'],-2,45,4.8]

print(names[6][1])
print(names[6][1:3])
print(len(names))

names[1]='shruti'
print(names)

names[4]='srija'
print(names)

print(len(names))

print(names.append("srinivas"))
print(names)
print(len(names))

names.append("sunil")
print(names)

names.append("prakash")
print(names)

names.pop()
print(names)

names.remove(45)
print(names)

names.pop(2)
print(names)
print(len(names))

names.extend("ondu")
print(names)
print(len(names))

names.pop()
print(names)

names.copy()
print(names)

print(names.count('s'))
print(names.count("srinivas"))

names.remove('sunil')
print(names)

print(names.reverse())