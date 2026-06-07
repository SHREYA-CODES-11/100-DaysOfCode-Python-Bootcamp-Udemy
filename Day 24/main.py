# Day 24
# Project 23

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("/Users/SHREYA JHA/Desktop/100 days of code/Day 24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("/Users/SHREYA JHA/Desktop/100 days of code/Day 24/my_file.txt", "w") as file:
#     file.write("New text.")

# with open("/Users/SHREYA JHA/Desktop/100 days of code/Day 24/my_file.txt", "a") as file:
#     file.write("\nNew text.")

# with open("/Users/SHREYA JHA/Desktop/100 days of code/Day 24/new_file.txt", "w") as file:
#     file.write("New text.")

# Project: Mail Merge
PLACEHOLDER  = "[name]"

with open("/Users/SHREYA JHA/Desktop/100 days of code/Day 24/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/Users/SHREYA JHA/Desktop/100 days of code/Day 24/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip() # removes white spaces from left and right sides of the content
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/SHREYA JHA/Desktop/100 days of code/Day 24/letter_for_{stripped_name}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)