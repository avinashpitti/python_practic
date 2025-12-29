# #1. Write a program to read 2 numbers from the keyboard and print sum?
# x=int(input("Enter first number : "))
# y=int(input("Enter second number : "))

# print("sum of x and y is : ",x+y)

# #2. How to read multiple values from the keyboard in a single line?
# x, y = map(int, input("Enter two numbers: ").split())
# print(x, y)

# #3. Program to check if a number is divisible by 7 or not?

# num=int(input("Check the value is divisible by 7 : "))

# if num % 7==0:
#     print("It is divisible by 7")
# else:
#     print("It is not divisible by 7")


# #4. Program to check if a number is multiple of 3 or not?

# num=int(input("Enter a number: "))

# if num % 3==0:
#     print("It's a multiple of 3")
# else:
#     print("It's not a multiple of 3")


# #5. Program to check if a number is positive or not?

# num=int(input("Enter a number: "))

# if num>0:
#     print("positive number")
# elif num ==0:
#     print("neither positive nor negative")
# else:
#     print("negative number")


# #6. Write a program to take a single digit number from the keyboard and print in english?

# num=int(input("Enter a single digit number (0-9) : "))

# digits={
#     0:'Zero',
#     1:'One',
#     2: 'Two',
#     3: 'Three',
#     4: 'Four',
#     5: 'Five',
#     6: 'Six',
#     7: 'Seven',
#     8: 'Eight',
#     9: 'Nine'
# }

# if num in digits:
#     print(digits[num])

# else:
#     print("Invalid input! Please enter a single digit!") 


# #7. Write a program to find the biggest of given 2 numbers from the command prompt?

# num1=int(input("Enter first number : "))

# num2=int(input("Enter second number : "))

# if num1 > num2: 
#     print("num1 is biggest")
# elif num2> num1:
#     print("num2 is biggest")
# else:
#     print("both are equal")

# #8. Write a program to find the biggest of given 3 numbers from the command prompt?

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if num1 > num2 and num1 > num3:
#     print(f"{num1} first number is the biggest")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} second number is the biggest")
# elif num3 > num1 and num3 > num2:
#     print(f"{num3} third number is the biggest")
# else:
#     print("Two or more numbers are equal")


# #9. Program to check if a number is a 3-digit number or not?

# user_input=int(input("Enter a 3 digit number: "))

# if  100 <= abs(user_input) < 1000 :
#     print(f"{user_input} is a 3 digit number")
# else:
#     print(f"{user_input} is not a 3 digit number")


# #10.Program to print even or odd for a given number from CMD/CLA?

# num=int(input("Enter a number: "))

# if num % 2==0:
#     print(f"{num} is an even number")
# else:
#     print(f'{num} is an odd number')

# #11.Program to print the greatest number in given two numbers?

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))

# if num1>num2:
#     print(f"{num1} i.e. first number is greatest")
# elif num2>num1:
#     print(f'{num2} i.e.. second number is greatest')
# else:
#     print(f'{num1} and {num2} are equal.')


# #12.Program to print the smallest number in given two numbers?

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))

# if num1 < num2 :
#     print(f'{num1} i.e.. firtst is smallest')
# elif num2 < num1 :
#     print(f'{num2} i.e.. second is smallest')
# else:
#     print(f'{num1} and {num2} are equal.')


#13.Program to print the greatest number in given three numbers?

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if num1> num2 and num1>num3:
    print(f"{num1}  i.e.. first number greatest")
elif num2>num1 and num2>num3:
    print(f'{num2} i.e.. second number greatest')
elif num3>num1 and num3>num2:
    print(f'{num3} i.e.. third number greatest')
else:
    print("Two or more values are equal.")

