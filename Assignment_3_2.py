# 1. Print given numbers of '*' or stars in a row

# n=int(input("Enter number of starts you want to print: "))
print(('*')*12)

print('-------------1---------------')

# 2. Print square pattern with 'A' symbols.
# A A A
# A A A
# A A A

for i in range(3):
    for j in range(3):
        print("A",end=' ')

    print()


print('------------2----------------')

# 3. Print square pattern with '*' symbols

for i in range(4):
    for j in range(4):
        print('*',end=' ')
    print()
    
print('-------------3---------------')

# 4. Print square pattern with given number/digit.
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5


for i in range(5):
    for j in range(5):
        print('5',end=' ')
    print()

print('------------4----------------')


# 5. Print square pattern with a given fixed digit in every row.
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

for i in range(1,5):
    for j in range(4):
        print(i,end=' ')
    print(i)

print('------------5----------------')


#6. Print square pattern with given digit in descending order.
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1

for i in range(5):
    for j in range(5):
        print(i,end=' ')
    print()

print('-----------6-----------------')


# #7. Print Right Angle Triangle pattern with '*' symbol.
# *
# * *
# * * *
# * * * *

# count=0
# for i in range(4):
#     for j in range(1):
#         count+=1
#     print('*'* count)

for i in range(1,5):
    print('* '*i)

print('-----------7-----------------')

# #8. Print Right AngleTriangle pattern with 'A' Symbol.
# A
# A A
# A A A
# A A A A


for i in range(1,5):
    print('A '*i)

print('-----------8-----------------')


# #9. Print Reverse Right Angle Triangle Pattern with ‘*’ Symbol
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5,0,-1):
    print('*'*i)

print('-----------9-----------------')

# #10.Print Right Angle Triangle with Fixed Alphabet Symbol
# A
# B B
# C C C
# D D D D

ch = 'A'# if we give space after A,TypeError: ord() expected a character, but string of length 2 found

for i in range(1,5):
    print((ch+' ')*i)
    ch=chr(ord(ch)+1)

print('-----------10-----------------')


# 11.Print right angle triangle with fixed digit symbol in every row
# 1
# 2 2
# 3 3 3
# 4 4 4 4

n=4

for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print()

print('-----------11-----------------')


# 12.Print Right Angle Triangle with Sequence of Digits - each row
# 1
# 1 2
# 1 2 3
# 1 2 3 4

count=0
for i in range(1,5):
    for j in range(1):
        count+=i
    print(count)