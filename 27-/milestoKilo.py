from tkinter import *


def calculate():
    miles = int(input.get())
    Km = miles * 1.60934
    kilometerResult.config(text = Km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height = 100)
window.config(padx=20,pady=20)

my_label = Label(text = "Miles", font = ("Arial", 12, "normal"))
my_label.grid(column = 2, row=0)

is_equal_to = Label(text = "is equal to", font = ("Arial", 12, "normal"))
is_equal_to.grid(column = 0, row=1)

Km = Label(text = "Km", font = ("Arial", 12, "normal"))
Km.grid(column = 2, row=1)

#Entry
input = Entry(width = 10)
input.grid(column =1, row = 0)

#so basically in the solutions she made the second entry a label, so it is easy to change
kilometerResult = Label(text = '0')
kilometerResult.grid(column =1, row = 1)

# #Entry
# input2 = Entry(width = 10)
# input2.grid(column =1, row = 1)

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column= 1, row = 2)

window.mainloop()