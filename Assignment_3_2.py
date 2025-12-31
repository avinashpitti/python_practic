# 1. Print given numbers of '*' or stars in a row

print('***********')

# 2. Print square pattern with 'A' symbols.
# A A A
# A A A
# A A A

for i in range(3):
    for j in range(3):
        print("A",end=' ')

    print()

for i in range(3):
    print('A B A')


# 3. Print square pattern with '*' symbols

for i in range(4):
    for j in range(4):
        print('*',end=' ')
    print()
    

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


# 5. Print square pattern with a given fixed digit in every row.
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

for i in range(1,5):
    for j in range(4):
        print(i,end=' ')
    print(i)

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

