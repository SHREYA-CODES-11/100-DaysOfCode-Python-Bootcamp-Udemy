# Day 16
# import turtle
# timmy = turtle.Turtle() # Turtle() is the class inside the turtle module
# timmy.shape("turtle") # timmy will change into the shape of an actual turtle
# timmy.color("red") # timmy will get red in colour
# timmy.forward(100)

# my_screen = turtle.Screen() # Screen() is another class inside the turtle module
# # or we can also code it as:
# # from turtle import Turtle, Screen
# # timmy = Turtle()
# # my_screen = Screen()
# print(my_screen.canvheight) # canvheight is an attribute under Screen()
# my_screen.exitonclick() # exitonclick() is a function under Screen() object

# prettytable package
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table.align)
# table.align = "l"
# print(table)  

# Day 17
# class User: # creating class
#     def __init__(self):
#         # initialise attributes
#         print("new user being created..")
#         pass
#     pass
# user_1 = User() # an object from that class
# user_1.id = "001"
# user_1.username = "shreya"
# print(user_1.username)

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user_1 = User("001", "shreya")
# user_2 = User("002", "rohan")
# # print(user_1.id)
# # print(user_1.username)
# # print(user_1.followers)
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

# Day 18
# #from turtle import * (to import every single functionality from turtle module)
# #import turtle as t (aliasing module name)
# from turtle import Turtle, Screen
# timmy = Turtle()
# #drawing a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# screen = Screen()
# screen.exitonclick()

# #drawing a dashed line
# import turtle as t
# tim = t.Turtle()
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# #drawing different shapes with different colors
# from turtle import Turtle, Screen
# import random
# tim = Turtle()

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "deepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):        
#         tim.forward(100)
#         tim.right(angle)

# for n in range(3,11): #for drawing shapes from triangle to decagon
#     tim.color(random.choice(colors))
#     draw_shape(n)

# screen = Screen()
# screen.exitonclick()

# #random walk program
# from turtle import Turtle, Screen
# import random
# tim = Turtle()

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "deepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed(0) #fastest speed
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# screen = Screen()
# screen.exitonclick()

# #drawing a spirograph
# import turtle as t
# import random
# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# tim.speed("fastest")

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5) #with a gap of 5 degree each time
# screen = t.Screen()
# screen.exitonclick()

# Project 18: Hirst Spot Painting
# hirst dots.jpef files belongs here
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('hirst dots.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# import turtle
# import random

# turtle.colormode(255)
# tim = turtle.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(199, 159, 114), (69, 91, 129), (148, 85, 52), (218, 210, 115), (136, 160, 193), (27, 32, 47), (179, 161, 35), (58, 33, 22), (184, 145, 164), (123, 70, 93), (137, 175, 153), (76, 115, 78), (143, 25, 15), (61, 30, 41), (187, 97, 82), (120, 28, 43), (46, 59, 94), (99, 118, 172), (178, 96, 114), (33, 51, 44), (99, 159, 85), (66, 84, 23), (215, 174, 192), (217, 181, 172), (218, 206, 7), (159, 210, 191)]

# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

# screen = turtle.Screen()
# screen.exitonclick()

# Day 19
# controlling the turtle with a key stroke
# from turtle import Turtle, Screen
# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key = "space", fun = move_forwards)
# screen.exitonclick()

# Project 19(a): Etch-a-Sketch
# from turtle import Turtle, Screen
# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home() #brings the turtle back at its starting point
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()

# Project 19(b): Turtle Racing Game
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet!", prompt = "Which turtle will win the race? Enter a colour: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0,7):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()