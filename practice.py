num=20
if num>10:
    print("The number is greater than 10")
    if num>20:
        print("The number is above 20 as well")
    else:
        print("But the number is below or equal to 20")

age=int(input("Enter your age: "))
has_license=input("Do you have license? (yes/no):").lower()=="yes"

if age>18:
    if has_license:
        print("You can drive")
    else:
        print("you need license to drive")
else:
    print("You are under age")


score=int(input("Enter your score: "))
attendance=int(input("Enter your attendance percentage: "))
submitted=input("Do you submitted your assignment? (yes/no)").lower()=="yes"

if score>60:
    if attendance>75:
        if submitted:
            print("you have passed in distinction due to assignment")
        else:
            print("you passed but no assignment submission")
    else:
        print("You just passed with low attendance and no assignment")
else:
    print("You failed the exam")

