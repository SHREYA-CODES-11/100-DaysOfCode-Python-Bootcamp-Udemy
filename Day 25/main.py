# Day 25

# with open("/Users/SHREYA JHA/Desktop/100 days of code/Day 25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# Working with csv module

# import csv
# with open("/Users/SHREYA JHA/Desktop/100 days of code/Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     # for row in data:
#     #     print(row)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Working with pandas library

# import pandas
# data = pandas.read_csv("/Users/SHREYA JHA/Desktop/100 days of code/Day 25/weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))
# # calculating mean: usual method
# print(sum(temp_list) / len(temp_list))
# # calculating mean using mean method
# print(data["temp"].mean()) # method under series
# # taking out maximum value out of the data
# print(data["temp"].max())

# # Get data of the columns
# print(data["condition"])
# print(data.condition)

# # Get data of the rows
# print(data[data.day == "Monday"])
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])
# print(data.temp == data.temp.max())

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Ajay", "Aman", "Chhavi"],
#     "scores": [76, 78, 80]
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_scores.csv")

import pandas
data = pandas.read_csv("/Users/SHREYA JHA/Desktop/100 days of code/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")