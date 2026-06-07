# Day 30
# Error Handling

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existence_key"]

try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    # file.close()
    # print("File was closed.")
    raise TypeError("This is an error that i amde up.")

# Example of raising an error

height = float(input("Height: "))
weight = int(input("Height: "))

if height > 3:
    raise ValueError("Human heights should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)