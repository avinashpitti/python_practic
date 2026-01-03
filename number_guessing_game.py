import random

secret=random.randint(1,10)

attempts=0

while True:
    guess = int(input("Enter a number(1-10) : "))

    if guess < 1 or guess > 10 :
        print("Invalid input! Enter a number b/w 1 and 10.")
        continue # skip counting attempt due to invalid output


    attempts+=1

    if guess == secret :
        print(f'you won in {attempts} attempts!')
        break
    elif guess > secret :
        print('Too high')
    elif guess < secret :
        print('Too low')


    