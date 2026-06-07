# Day 26
# List Comprehensions

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# The above code is the replacement of the below code (using list comprehension)
nums = [5, 6, 7]
new_nums = []
for i in nums:
    i += 1
    new_nums.append(i)
print(new_nums)

# Example 2

name = "Shreya Jha"
new_list = [letter for letter in name]
print(new_list)

# Example 3

ran = [r * 2 for r in range(1, 5)]
print(ran)

# Conditional List Comprehensions

names = ["Aman", "Beth", "Chetna", "Dhriti", "Shreya", "Vishal"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

caps = [n.upper() for n in names if len(n) > 5]
print(caps)

# Example 2

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(item) for item in list_of_strings]
result = [i for i in numbers if i % 2 ==0]
print(result)

# Dictionary Comprehensions

import random
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

# use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)

# using Dictionary Comprehensions with pandas

student_dict = {
    "student": ["Angela", "Shreya", "Vishal"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop throght a data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Shreya":
        print(row.score)