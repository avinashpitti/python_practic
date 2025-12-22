# #1
# a = 10
# b = 20
# c = a + b
# print(c)

# print(type(c))
# d=str(c)
# print(type(d))

# #2

# x = "100"
# y = 20
# z=int(x)+ y
# print(z)
# print(type(z))

# z=float(z)
# print(type(z))

# #3

# a=0
# b=5

# print(bool(a))
# print(bool(b))

# print(a<b and b>0)

# #4

# s = "python developer"
# print(s[0])
# print(s[-1])
# print(s[7:])
# print(s[::-1])

# #5

# s = "  Learn Python Fast. Python is an important programming language. " 
# s=s.strip()
# print(s.upper())
# print(s.replace("Python","Django",1))

# #6
# email = "avinash@gmail.com"
# if "@" in email:
#     print("yes")

# # if "gmail.com" in email:
# #     print("yes")

# if email.endswith("gmail.com"):
#     print("yes")

# #7.

# nums = [10, 20, 30, 40, 50]
# nums.append(60)
# print(nums)

# nums.remove(30)
# print(nums)

# print(len(nums))
# print(nums[-3:])

# #8

# nums = [1, 2, 3, 4, 5]
# squares=[]
# for i in nums:
#     squares.append(i*i)
# print(squares)

# #method:2
# nums=[1,2,3,4,5]
# squares=[i*i for i in nums]
# print(squares)

#9

data = [10, "python", 3.5, True]

for el in data:
    if type(el)==int:
        print(el)

for el in data:
    print(type(el))

# #10

# t = (10, 20, 30)
# # t[1]=25 # TypeError: 'tuple' object does not support item assignment
# # print(t)

# l=list(t)
# print(l)
# l[1]=25
# print(l)
# t=tuple(l)
# print(t)

# #11

# a = {10, 20, 30, 40}
# b = {30, 40, 50, 60}

# print(a.intersection(b))

# for ele in a:
#     print(a-b)

# print(a.union(b))

# #12

# student = {
#     "name": "Avinash",
#     "age": 22,
#     "course": "BCA"
# }

# print(student.keys())
# print(student.values())

# student["college"]="ABC"
# print(student)

# student["age"]=23

# print(student)

# #13

# marks = {
#     "python": 80,
#     "java": 70,
#     "sql": 75
# }

# print(marks.keys())
# print(marks.values())

# for subject, score in marks.items():
#     print(subject,"->",score)

# #14

# prices = {
#     "apple": 100,
#     "banana": 40,
#     "orange": 60
# }

# max_item = max(prices, key=prices.get)
# print(max_item)

# for item in prices:
#     prices[item] += 10

# print(prices)


# #15

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
# # a changes because a=b

# #16

# x = (1, 2, 3) # It's a tuple which can't be mutable
# y = list(x) # So we changed it into a list which is mutable
# y.append(4) # Then added an element to the list
# print(x, y) # now printing both tuple and list
 

# #17

# # d = {
# #     [1, 2]: "hello" # Typeerror: unhashable type : List
# # }




