# Day 27
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx = 20, pady = 20) # space around the edges

# Label

my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
# my_label.pack() # this method will get(pack) the label onto the centre of the screen
# my_label.pack(side = "left") 
# my_label.pack(side = "bottom")
# my_label.pack("right")
# my_label.pack(expand = True)

# my_label.place(x = 0, y = 0) # place specifies the coordinates where the widget is needed to be specifically placed

my_label.grid(column = 0, row = 0)

my_label["text"] = "New Text"
my_label.config(text = "New Text")

# Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)

button = tkinter.Button(text  = "Click Me", command = button_clicked)
# button.pack()
button.grid(column = 1, row = 1)

new_button = tkinter.Button(text = "New Button")
new_button.grid(column = 2, row = 0)

# Entry

input = tkinter.Entry(width = 10)
# input.pack()
input.grid(column = 3, row = 2)
print(input.get())

window.mainloop()