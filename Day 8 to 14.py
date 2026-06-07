# Day 8
# def greet(name):  # 'name' is the parameter
#     print("I am learning new concepts.")
#     print(f"{4+5} hi {name}")
#     print("hello shreya!")
# greet("girl")  # 'girl' is the argument

# method 1
# def life_in_weeks():
#     current_age = int(input("Enter your current age: "))
#     age = 90
#     years_left = age - current_age
#     weeks_left = years_left * 52
#     print(f"You have {weeks_left} weeks left.")
# life_in_weeks()

# method 2: with parameters and arguments
# def life_in_weeks(age):
#     years_remaining = 90 - age
#     weeks_remaining = years_remaining * 52
#     print(f"You have {weeks_remaining} weeks left.")
# life_in_weeks(12)

# Love Calculator
'''def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("r")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
calculate_love_score("Kanye West", "Kim Kardashian")'''

# Caesar cipher
# print("Welcome to Caesar Cipher!")
# print('''
        
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
#             88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
#               88                                             
#               88           
# ''')
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# # encryption
# # def encrypt(original_text, shift_amount):
# #     cipher_text = ""

# #     for letter in original_text:
# #         shifted_position = alphabet.index(letter) + shift_amount
# #         shifted_position %= len(alphabet) # to overcome index out of range problem
# #         cipher_text += alphabet[shifted_position]

# #     print(f"Here's the encoded result: {cipher_text}")

# # encrypt(original_text = text, shift_amount = shift)

# # decryption
# # def decrypt(original_text, shift_amount):
# #     output_text = ""

# #     for letter in original_text:
# #         shifted_position = alphabet.index(letter) - shift_amount
# #         shifted_position %= len(alphabet) # to overcome index out of range problem
# #         caesar_text += alphabet[shifted_position]

# #     print(f"Here's the decoded result: {output_text}")

# # decrypt(original_text = text, shift_amount = shift)

# def caesar(original_text, shift_amount, encode_decode):
#     output_text = ""
#     if encode_decode == "decode":
#         shift_amount *= -1

#     for letter in original_text:

#         if letter not in alphabet:
#             output_text += letter
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet) # to overcome index out of range problem
#             output_text += alphabet[shifted_position]

#     print(f"Here's the {encode_decode}d result: {output_text}")
# caesar(original_text = text, shift_amount = shift, encode_decode = direction)

# should_continue = True
# while should_continue:

#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     caesar(original_text = text, shift_amount = shift, encode_decode = direction)

#     restart = input("Type 'yes' if you want to continue. Otherwise, type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye!")

# Day 9
# my_dict = {
#     "alphabet":"There are 26 alphabets in the English language.",
#     "Sanskrit":"It is the mother of all the languages.",
#     "India":"It is a democratic country.",
# }
# print(my_dict["India"])
# my_dict["Delhi"] = "It is the capital city of India."
# print(my_dict)

'''student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)'''

# Project 9: Secret Auction Program
# print("Welcome to the Secret Auction Program!")
# print('''
#      T                                    \`.    T
#      |    T     .--------------.___________) \   |    T
#      !    |     |//////////////|___________[ ]   !  T |
#           !     `--------------'           ) (      | !
#                                            '-'      !
# ''')

# def find_highest_bidder(bidding_dictionary):
#     winner = ""
#     highest_bid = 0
#     # or directly: max(bidding_dictionary)
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}.")

# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?\n")
#     price = float(input("How much do you want to bid?\n$"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 100) # to clear the screen

# Day 10
# def name(f_name, l_name):
#     print(f_name.title(), end = ' ') # title() converts the string in the pascal or title case
#     print(l_name.title())
# name("shreya", "JHA")

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# is_leap_year(2024)

# Project 10: The Calculator project
# print('''
#  _____________________
# |  _________________  |
# | | PYTHONISTA   0. | |
# | |_________________| |
# |  ___ ___ ___   ___  |
# | | 7 | 8 | 9 | | + | |
# | |___|___|___| |___| |
# | | 4 | 5 | 6 | | - | |
# | |___|___|___| |___| |
# | | 1 | 2 | 3 | | x | |
# | |___|___|___| |___| |
# | | . | 0 | = | | / | |
# | |___|___|___| |___| |
# |_____________________|       
#            _            _       _             
#           | |          | |     | |            
#   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
#  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
# | (_| (_| | | (__| |_| | | (_| | || (_) | |   
#  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                  
# ''')
# def add(n1, n2):
#     return n1 + n2
# def subtract(n1, n2):
#     return n1 - n2
# def multiply(n1, n2):
#     return n1 * n2
# def divide(n1, n2):
#     return n1 / n2
# operations = {
# "+": add,
# "-": subtract,
# "*": multiply,
# "/": divide,
# }
# # print(operations["*"](4,8))

# def calculator():
#     should_accumulate = True
#     num1 = float(input("Enter the first number: "))

#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Choose a mathematical operation: ")
#         num2 = float(input("Enter the second number: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         choice = input("Type 'y' to continue with {answer}, or type 'n' to start a new calculation. ").lower()
#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20) # an illusion to clear the screen
#             calculator() # recursion: calling function within the function itself
# calculator()

# Day 11
# Blackjack Project
# import random

# def deal_card():
#     """Returns a random card from the deck""" # Docstring 
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # 11 is the ACE card
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """Take a list of cards and return the score calculated from the cards""" # Docstring
#     if sum(cards) == 21 and len(cards) == 2: # or if 11 in cards and 10 in cards and len(cards) == 2:
#         return 0 # 0 to represent an ACE card which is 11
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)   
    
#     return sum(cards)

# def compare(u_score, c_score): # right click on the word which needs to be renamed in the code and click on rename object and then enter
#     if u_score == c_score:
#         return "Draw"
#     elif c_score == 0: # that means it is an ACE card or a BlackJack
#         return "You lose, opponent has a BlackJack!"
#     elif u_score == 0:
#         return "You win with a BlackJack!"
#     elif u_score > 21:
#         return "You went over 21, you lose!"
#     elif c_score > 21:
#         return "Opponent went over 21, you win!"
#     elif u_score > c_score:
#         return "You win!"
#     else:
#         return "You lose!"

# def play_game():
#     print('''
#      _     _            _        _            _
#     | |   | |          | |      (_)          | |
#     | |__ | | __ _  ___| | __    _  __ _  ___| | __
#     | '_ \| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
#     | |_) | | (_| | (__|   <    | | (_| | (__|   <
#     |_.__/|_|\__,_|\___|_|\_\   | |\__,_|\___|_|\_\_
#                             _/ |    
#                             |__/               
#                         .------.
#     .------.           |A .   |
#     |A_  _ |    .------; / \  |
#     |( \/ )|-----. _   |(_,_) |
#     | \  / | /\  |( )  |  I  A|
#     |  \/ A|/  \ |_x_) |------'
#     `-----+'\  / | Y  A|
#             |  \/ A|-----'    
#             `------'
#     ''')
#     print("Welcome to the game of BlackJack!")
#     user_cards = []
#     computer_cards = []
#     computer_score = -1 # just in case the 1st while loop doesn't get the chance to be executed, then till the 2nd while loop computer_score variable will remain undefined there
#     # we can't assign 0 to computer_score as 0 here means an ACE card
#     user_score = -1 # just as similar as computer_score
#     is_game_over = False

#     for _ in range(2):# It is going to loop through the function to chhose a card
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())

#     while not is_game_over: # 1st while loop
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards: {user_cards}, current scores: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score != 0 and computer_score < 17: # 2nd while loop
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Coputer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))

# while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == "y":
#     # print("\n" * 100) # to clear the console
#     play_game()

# Day 12
# Local scope and Global scope of variables

# def is_prime(num):
#     if num == 2:
#         return True
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# print(is_prime(5))

# enemies = 1
# def increase_enemies():
#     global enemies # making the variable enemies the global one so that it can refer to the global variable which is initialised outside the function
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# Number Guessing Project
# import random

# EASY_LEVEL_TURNS = 10 # global variables
# HARD_LEVEL_TURNS = 5

# def check_answer(user_guess, actual_answer, turns):
#     """Checks answer against guess, returns the number of turns remaining."""
#     if user_guess > actual_answer:
#         print(f"Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print(f"Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! It's {actual_answer}.")

# def set_difficulty():
#     level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
    
# def game():
#     print('''
#         _                         ___  _                 _
#       / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
#      / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
#     / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
#     \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    
#     ''')
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = random.randint(1, 100)
#     # print(answer)

#     turns = set_difficulty()

#     guess = 0 
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: ")) 
#         turns = check_answer(guess, answer, turns) # to update the local variable turns to check the answer
#         if turns == 0:
#             print("You've run out of guesses, you lose!")
#             return # to stop the game when turns = 0
#         elif guess != answer:
#             print("Guess again.")
# game()

# Day 13
# try and except block
# try:
#     age = int(input("What is your age? "))
# except ValueError:
#     print("You have entered an invalid input. Try entering a numerical value instead.")
#     age = int(input("What is your age? "))
# if age > 18:
#     print("You can drive.")

# import random

# def add(x, y):
#     return x + y

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1,3)
#         new_item = add(new_item, item)
#     # b_list.append(new_item) # outside for loop it does work as expected
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])

# Day 14
import random
# Game data
data = [
    {
        'name': 'Instagram',
        'follower_count': 685,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 648,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 376,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 395,
        'description': 'Actor and Profession Wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 422,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 394,
        'description': 'Reality TV Actress and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 358,
        'description': 'Reality TV Actress and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Khloe Kardashian',
        'follower_count': 304,
        'description': 'Actress and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 76,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Maluma',
        'follower_count': 65,
        'description': 'MUsician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 89,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 77,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 92,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 55,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 270,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 71,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 73,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'NASA',
        'follower_count': 96,
        'description': 'Space Agency',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 103,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Victoria\'s Secret',
        'follower_count': 79,
        'description': 'Lingrie Brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 180,
        'description': 'Actress and Musician',
        'country': 'United States'
    },
    {
        'name': 'Drake',
        'follower_count': 143,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Shakira',
        'follower_count': 90,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Rihanna',
        'follower_count': 150,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 135,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 171,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 137,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 177,
        'description': 'Comedian and Actor',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 220,
        'description': 'Reality TV Personality',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 204,
        'description': 'Singer and Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 294,
        'description': 'Singer and Actor',
        'country': 'Canada'
    },
    {
        'name': 'Hailey Bieber',
        'follower_count': 54,
        'description': 'Businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 282,
        'description': 'Singer',
        'country': 'United States'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 121,
        'description': 'Singer and Musician',
        'country': 'United States'
    },
    {
        'name': 'Jimmy Fallon',
        'follower_count': 27,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Sachin Tendulkar',
        'follower_count': 49,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Amitabh Bachchan',
        'follower_count': 37,
        'description': 'Actor',
        'country': 'India'
    },
    {
        'name': 'Alia Bhatt',
        'follower_count': 86,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Cardi B',
        'follower_count': 164,
        'description': 'Actress and Model',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 504,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Salman Khan',
        'follower_count': 69,
        'description': 'Actor',
        'country': 'India'
    },
    {
        'name': 'Diljit Dosanjh',
        'follower_count': 25,
        'description': 'Actor and Singer',
        'country': 'India'
    },
    {
        'name': 'Yo Yo Honey Singh',
        'follower_count': 17,
        'description': 'Rapper and Musician',
        'country': 'India'
    },
    {
        'name': 'Neha Kakkar',
        'follower_count': 78,
        'description': 'Singer',
        'country': 'India'
    },
    {
        'name': 'Arijit Singh',
        'follower_count': 11,
        'description': 'Singer and Musician',
        'country': 'India'
    },
    {
        'name': 'Brad Pitt',
        'follower_count': 2,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Angelina Jolie',
        'follower_count': 15,
        'description': 'Actress and Model',
        'country': 'United States'
    },
    {
        'name': 'Deepika Padukone',
        'follower_count': 80,
        'description': 'Actress and Model',
        'country': 'India'
    },
    {
        'name': 'MrBeast',
        'follower_count': 65,
        'description': 'YouTuber',
        'country': 'United States'
    },
]

def format_data(account):
    """Formatting the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a" # returns True if user_guess is "a"
        # or
        # if user_guess == "a":
        #     return True
        # else:
        #     return False
    else:
        return user_guess == "b" # returns True if user_guess is "b"

print('''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/      
''')

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b: # if in case both the choices are same, we need different choice for account_b 
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print('''
     _  _  ___ 
    ( \/ )/ __)
     \  / \__ \\
      \/  (___/
    ''')
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}.")
    else:
        print(f"Sorry but you're wrong! Final score: {score}.")
        game_should_continue = False
