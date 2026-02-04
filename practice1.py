# # sum of nums from 1 to n.

# num=int(input("Enter a number : "))
# def sum_of_nums(num):
#     total=0
#     for i in range(1,num+1):
#         total+=i
#     return total
# print(sum_of_nums(num))


# # method 2 :

# n=int(input("Enter a number : "))
# def sum_nums(n) :
#     return n*(n+1)//2
# total=sum_nums(n)
# print(total)


# sum of first n odd numbers

n=int(input("Enter a number : "))
def sum_odd_nums(n):
    return n**2
total=sum_odd_nums(n)
print(total)

# sum of first n odd numbers

num=int(input('Enter a number : '))
def sum_odd_nums(n):
    total=0
    for i in range(1,2*n,2):
        total+=i
    return total
print(sum_odd_nums(n))



    
    


