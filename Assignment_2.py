# PART 1

#1. Generate a random integer between 1 and 100.

import random

print(f'random integer b/w 1 and 100 : {random.randint(1,100)}')

print('--------------1 Done----------------')

#2. Generate a random floating point between 0 and 1.

print(f'random float value b/w 0 and 1 : {random.random()}')

print('--------------2 Done----------------')


#3. Generate a random even number between 50 and 100

num=random.randrange(50,101,2)
print(f'random even number b/w 50 and 100 :  {num}')

print('--------------3 Done----------------')


#4. print 5 random numbers between 10 and 50 using a loop

print("5 random numbers between 10 and 50 : ")
for i in range(5):
    num = random.randint(10, 50)
    print(num)

print('--------------4 Done----------------')


#5. create a list of 10 random integers between 1 and 100, and print them all.

# random.sample(sequence, k)

print(random.sample(range(1, 101), 10))

print('--------------5 Done----------------')

print('--------------PART A Done----------------')


# PART 2 : Random choices from Lists

#1. create a list of fruits and print a random fruit each time you run the program

fruits=['apple','kiwi','banana','cherry','dragon','orange']

print(random.choice(fruits))

print('--------------1 Done----------------')


#2. Randomly select 3 students from a list of 10 names for a project

students=['avi','amar','srija','srinu','sruthi','chandu','bablu','kasi','priya','anil']

print(random.sample(students,k=3))

print('--------------2 Done----------------')

#3. shuffle a list of numbers from 1 to 10 and print the shuffled result.

nums=list(range(1,11))
random.shuffle(nums)
print(nums)

print('--------------3 Done----------------')

#4. From a list of 20 numbers,select 5 random numbers without replacement

numbers=list(range(1,21))
#“I used random.sample() to ensure unique selection without replacement(no duplicates).”
print(random.sample(numbers,k=5))

print('--------------4 Done----------------')

#5. create a color palette (["red","blue","green","yellow","black","white"]) and randomly 
# select a color.

colors=["red","blue","green","yellow","black","white"]

print(random.choice(colors))

print('--------------5 Done----------------')

#PART 3 : SIMULATION TASKS

#1. Dice roll simulation
# simulate rolling a 6 sided die 10 times and print each result

for i in range(1,11):
    roll=random.randint(1,6)
    print(f'roll {i} : {roll}')

print('--------------1 Done----------------')


#2. Coin Flip Simulation
# Simulate flipping a coin 100 times and count how many times it landed on Heads vs Tails.
head_count=0
tail_count=0
for i in range(100):
    flip = random.choice(['Head','Tail'])

    if flip=="Head":
        head_count+=1
    elif flip=="Tail":
        tail_count+=1


print("Heads:",head_count)
print("Tails:",tail_count)

if head_count > tail_count :
    print("head wins")
elif head_count == tail_count:
    print('tied')

else:
    print('tail wins')

print('--------------2 Done----------------')


#3.Lottery Number Generator
# Generate 6 unique random numbers b/w 1 and 49.
lottery =random.sample(range(1,50),k=6)
print('lottery numbers: ', *lottery)
# * is called the unpacking operator
# It unpacks the list elements one by one

print('--------------3 Done----------------')



#4. Password Generator

# create a random 10 character password using:
# uppercase, lowercase letters, digits, and special symbols.

import string

# all characters

uppercase=string.ascii_uppercase
# string.ascii_letters=string.ascii_lowercase + string.ascii_uppercase
#But it doesn't guarantee atleast one lowercase and one uppercase
lowercase=string.ascii_lowercase
digits=string.digits
symbols=string.punctuation


# combine all characters

all_chars=uppercase+lowercase+digits+symbols

# generate password

password=''.join(random.sample(all_chars,10))
print("Generated password", password)

print('--------------4 Done----------------')


#5. Guess the number game
# The computer picks  a random number between 1 and 50
# The user keeps guessing until they find it.
# print "Too High" or "Too Low" hints after each guess.



# computer chooses a number
secret_number = random.randint(1, 50)

attempts = 0

while True:
    guess = int(input("Guess a number b/w 1 and 50 : "))
    attempts += 1

    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print(f"Correct! You guessed it in {attempts} attempts 🎉")
        break

print('--------------5 Done----------------')



#  PART 4 : BONUS CHALLENGE

#1. Random sentence generator
# create 3 lists --- subjects, verbs, objects  --- and randomly combine them to form
# funny sentences like : "My cat eats pizza."



subjects = ["My cat", "A dog", "The teacher", "My friend", "A robot"]
verbs = ["eats", "kicks", "throws", "loves", "hates"]
objects = ["pizza", "a ball", "homework", "ice cream", "the laptop"]

sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."

print(sentence)

print('--------------1 Done----------------')


#2. Rock-paper- scissors- game
# Let the user choose Rock, Paper or Scissors
# The computer makes a random choice
# Display who wins

choices=['rock','paper','scissors']

user_choice=input("Choose Rock, Paper or Scissors: ").lower()
computer_choice=random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if computer_choice==user_choice:
    print("It's a tie.")
elif(
    (user_choice=='rock' and computer_choice=='scissors') or
    (user_choice=='paper' and computer_choice=='rock') or
    (user_choice=='scissors' and computer_choice=='paper')
):
    print("you win!")
else:
    print('computer wins!')


print('--------------2 Done----------------')


#3. Dice game b/w two players

# Both players roll a die 5 times each
# print each roll and determine the winner based on the total score.


player1_total = 0
player2_total = 0

print("Player 1 rolls:")
for _ in range(5):
    roll = random.randint(1, 6)
    player1_total += roll
    print(roll)

print("\nPlayer 2 rolls:")
for _ in range(5):
    roll = random.randint(1, 6)
    player2_total += roll
    print(roll)

print("\nTotal Scores:")
print("Player 1:", player1_total)
print("Player 2:", player2_total)

if player1_total > player2_total:
    print("Player 1 Wins 🎉")
elif player2_total > player1_total:
    print("Player 2 Wins 🎉")
else:
    print("It's a Tie 🤝")







 
    





