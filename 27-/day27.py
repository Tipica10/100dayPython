from tkinter import *

def button_clicked():
    my_label['text'] = input.get()

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height = 300)
window.config(padx=20,pady=20)
#Label

my_label = Label(text = "I am a Label", font = ("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column = 0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column= 1, row = 1)

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column= 2, row = 0)
#Entry
input = Entry(width = 10)
input.grid(column =4, row = 3)















# #why aren't the arguments of a function listed for pack
# like other arguments
# because of (**kw)
# when you hover over a function...
# sometimes the arguments have default values when
# they have an = sign next to them when u hover

# def calculate (**kwargs):
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#
# #allows any number of arguments
# #type of kwargs is dictionary
#
# calculate(add=3, mult=5)









window.mainloop()