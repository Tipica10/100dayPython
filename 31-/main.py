import pandas
import random
from tkinter import *

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
french_list_random = {}
to_learn = {}

try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("data/french_words.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")


def new_word():
    global french_list_random, flip_timer
    window.after_cancel(flip_timer)
    french_list_random = random.choice(to_learn)
    canvas.itemconfig(lang, text='French', fill ='black')
    canvas.itemconfig(word, text= french_list_random['French'], fill ='black')
    canvas.itemconfig(background, image=card_front_image)
    flip_timer = window.after(3000, card_back)

def clicked_correct():
    to_learn.remove(french_list_random)
    new_word()

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


def card_back():
    canvas.itemconfig(background, image=card_back_image)
    canvas.itemconfig(lang, text='English', fill ='white')
    canvas.itemconfig(word, text=french_list_random['English'], fill ='white')


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, card_back)

canvas = Canvas(width =800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400,260, image= card_front_image)


lang = canvas.create_text(400,150,text="",font=("Arial",30,"italic"))
word = canvas.create_text(400,263,text="",font=("Arial",45,"bold"))
canvas.grid(column=0,row=0, columnspan = 2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image= right_image, highlightthickness=0, command=clicked_correct)
right_button.grid(column=0,row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image= wrong_image, highlightthickness=0, command=new_word)
wrong_button.grid(column=1,row=1)

new_word()


window.mainloop()