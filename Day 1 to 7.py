'''#Day 1
print("Hello World!") #print function
input("What is your name?") #input function
print("Hello "+input("What is your name?")) #concatenation

# ctrl+'/' to make a line a comment

a=("Hello World") #variable
print(len(a)) #length function

#Project 1: Band Name Generator
print("Welcome to the Band Name Generator!")
city=input("Which city did you grow up in?\n")
pet=input("What is the name of your pet?\n")
print("Your band name could be: "+city+" "+pet)'''

#Day 2
'''print("Hello"[1]) #Subscripting of string
print(type("hello")) #type function: type checking
print(int("1234")) #type conversion or casting

#BMI calculator
height = 1.65 
weight = 84
bmi = weight/height**2
print(bmi)
print(int(bmi)) #converting in an integer
print(round(bmi)) #rounding or flooring the output
print(round(bmi,2)) #rounding till 2 decimal places
print(f"Your BMI is = {bmi}") #f string

#Project 2: Tip Calculator
print("Welcome to the Tip calculator!")
bill=float(input("What is your total bill?\n$"))
tip=int(input("What percentage tip would you like to give? 10 or 12 or 15\n"))
people=int(input("How many people are splitting the bill?\n"))
total_bill = tip / 100 * bill + bill
#or 
#tip_as_percent = tip / 100
#total_tip_amount = bill* tip_as_percent
#total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount} ")'''

#Day 3
'''print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: #elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    photo = input("Do uou want a photo? Type y for yes and n for no.")
    if photo == 'y':
        #Add $3 to the bill
        bill += 3 #bill = bill + 3
    print(f"Your final bill is: {bill}")
else:
    print("Sorry! This ride is not for you.")

weight = float(input("What is your weight in kgs? "))
height = float(input("What is your height in cms? "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("You are underweight!")
elif bmi > 18.5 and bmi < 25:
    print("You are normal weight!")
else:
    print("You are overweight!")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepporoni on your pizza? Y or N: ")
cheese = input("Do you want extra cheese on your pizza? Y or N: ")
if size == 'S':
    bill = 15
    print("Small pizza costs $15.")
    if pepperoni == 'y':
        bill += 2
    if cheese == 'y':
        bill +=1
elif size == 'M':
    bill = 20
    print("Medium pizza costs $20.")
    if pepperoni == 'y':
        bill += 3
    if cheese == 'y':
        bill +=1
elif size == 'L':
    bill = 25
    print("Large pizza costs $25.")
    if pepperoni == 'y':
        bill += 3
    if cheese == 'y':
        bill +=1
else:
    print("You typed the wrong inputs!")
print(f"Your total bill is: ${bill}")'''

#Project 3: Treasure Island
'''print(\'''      #to remove the comment we need to remove the '\' inside the print statement
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/ 
*******************************************************************************\''')
print("Welcome to the Treasure Island!\nYour mission is to find the treasure....")
choice1 = input("You're at a crossroad, where do you want to go?\nType L for \"left\" or type R for \"right\". ").lower()
if choice1 == "l":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake.\n"
                    "Type \"wait\" to wait for a boat or type \"swim\" to swim through the lake. ").lower()
    if choice2 == "wait":
        choice3 = input("You've safely arrived the island.\nThere is a house with 3 doors: One red, one yellow and one blue.\n"
                        "Which colour do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over!")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("There is no such door. Game Over!")
    else:
        print("You got attacked by an angry crocodile. Game Over!")
else:
    print("You fell into a hole. Game Over!")'''

#Day 4
# import random
# random_int = random.randint(1, 10) #1 & 10 both included
# print(random_int)
# random_real = random.random() #0 is included but 1 is not included
# print(random_real)
# random_float = random.uniform(1,10) #1 & 10 both included
# print(random_float)
'''heads_tails = random.randint(0,1)
if heads_tails == 0:
    print("Heads!")
else:
    print("Tails!")'''

'''friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"] #list
#Option 1
pay_the_bill = random.randint(1,5) 
if pay_the_bill == 1:
    print(friends[0])
elif pay_the_bill == 2:
    print(friends[1])
elif pay_the_bill == 3:
    print(friends[2])
elif pay_the_bill == 4:
    print(friends[3])
else:
    print(friends[4])
#Option 2    
print(random.choice(friends))
#Option 3
random_index = random.randint(0,4)
print(friends[random_index])'''

# Project 4: Rock, Paper, Scissors
# Method 1
'''import random
print("Welcome to the game of Rock, Paper, Scissors!")
rock = \'''
    _______
   /\| | | |
  / /|_|_|_|
  \        |
   \_______/
\'''
paper = \'''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
\'''
scissors = \'''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
\'''
user_choice = int(input("Type 0 for 'rock', 1 for 'paper' and 2 for 'scissors'.\n"))
computer_choice = random.randint(0,2)
if user_choice == 0:
    print(rock)
    print(f"Computer chose: {computer_choice}")
    if computer_choice == 1:
        print(paper)
        print("You lose!")
    elif computer_choice == 2:
        print(scissors)
        print("You win!")
    else:
        print(rock)
        print("Match draw!")
elif user_choice == 1:
    print(paper)
    print(f"Computer chose: {computer_choice}")
    if computer_choice == 0:
        print(rock)
        print("You win!")
    elif computer_choice == 2:
        print(scissors)
        print("You lose!")
    else:
        print(paper)
        print("Match draw!")
elif user_choice == 2:
    print(scissors)
    print(f"Computer chose: {computer_choice}")
    if computer_choice == 0:
        print(rock)
        print("You lose!")
    elif computer_choice == 1:
        print(paper)
        print("You win!")
    else:
        print(scissors)
        print("Match draw!")
else:
    print("Invalid choice. Play again.")'''

# Method 2: uses lesser lines of code
'''import random
print("Welcome to the game of Rock, Paper, Scissors!")
rock = \'''
    _______
   /\| | | |
  / /|_|_|_|
  \        |
   \_______/
\'''
paper = \'''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
\'''
scissors = \'''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
\'''
game_images = [rock, paper, scissors]
user_choice = int(input("Type 0 for 'rock', 1 for 'paper' and 2 for 'scissors'.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:\n")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("Invalid choice. Play again.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("Match draw!")'''

#Day 5
# scores = [195, 89, 77, 95, 100, 110, 116, 180, 155, 55, 81, 34, 129, 198, 200, 68]
# sum = 0
# for score in scores:
#     sum += score
# print(sum) #or directly sum() method can be used: sum(scores)

# max_score = 0 
# for score in scores:
#     if score > max_score:
#         max_score = score
# print(max_score) #or direct: print(max(scores))

# total = 0
# for number in range (1, 101):
#     total += number
# print (total)

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:    
#         print(number)

#Project 5: PyPassword Generator
'''import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+', '-', '/']
print("Welcome to the PyPassword Generator!")
let = int(input("How many letters do you want in your password?\n"))
num = int(input("How many numbers do you want in your password?\n"))
sym = int(input("How many symbols do you want in your password?\n"))
# Easy level: [letters, numbers, symbols] gets printed in this order only
# for ran_let in range(1, let + 1): #or range(0, let)
#     print(random.choice(letters), end = '')
# for ran_num in range(1, num + 1): #or range(0, num)
#     print(random.choice(numbers), end = '')
# for ran_sym in range(1, sym + 1): #or range(0, sym)
#     print(random.choice(symbols), end = '')

# Hard level: all the characters gets mixed up
password = []
for ran_let in range(0, let): 
    password.append(random.choice(letters))
for ran_num in range(0, num):
    password.append(random.choice(numbers))
for ran_sym in range(0, sym):
    password.append(random.choice(symbols))
random.shuffle(password)
# print(password)
# converting above list into a password string
pass_str = ""
for char in password:
    pass_str += char
print(f"Your strong password is: {pass_str}")'''

#Day 6: Dedicated to Reeborg's Maze
# def my_function():
#     print("Hello")
#     print("Bye")
# my_function()

#Day 7
# Project 7: Hangman
import random
stages = ['''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / \
     |
  ___|___
''', '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / 
     |
  ___|___
''', '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |      
     |
  ___|___
''', '''
      _______
     |/      |
     |       O
     |      \|
     |       |
     |      
     |
  ___|___
''', '''
      _______
     |/      |
     |       O
     |       |
     |       
     |      
     |
  ___|___
''', '''
      _______
     |/      |
     |       
     |       
     |       
     |      
     |
  ___|___
''']
print("Welcome to the game of HANGMAN!") # we can create separate modules in different files for storing the images used and the list of words to make the code tidy.
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
                                       ''')

lives = 5

words_list = ["apple", "banana", "camel", "dodger", "emanuel", "fallacy", "ghosting", "haunted", "igloo", "jamalkudu", "kalipahadi", "lemonjuice", "manual", "namaste", "operahouse", "panamaisland"]
chosen_word = random.choice(words_list)
# print(chosen_word)

placeholder = ""                     # blank = "_"
word_length = len(chosen_word)       # for letter in chosen_word:
for position in range(word_length):  #     print(blank, end = ' ')
    placeholder += "_"  
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    print(f"**********************{lives}/5 LIVES LEFT**********************")
    guess = input("\nGuess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'")
    
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter) # we can also append the 'guess' because at this point, they both are same
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"************IT WAS {chosen_word}! YOU LOSE************")

    if "_" not in display:
        game_over = True
        print("************YOU WIN************") 

    print(stages[lives]) # to print hangman ascii art