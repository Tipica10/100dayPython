from tkinter import *
import math

from wcwidth.table_grapheme import GRAPHEME_REGIONAL_INDICATOR

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_t = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_t)
    canvas.itemconfig(timer, text= "00:00")
    Timer_label.config(text="Timer",font=(FONT_NAME,35,"bold"), fg= GREEN, bg=YELLOW)
    checkmark_label.config(text= "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        Timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        Timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        Timer_label.config(text ="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_minutes = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer, text = f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer_t
        timer_t = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text= marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


canvas = Canvas(width =200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomato)
timer = canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

Timer_label = Label(text="Timer",font=(FONT_NAME,35,"bold"), fg= GREEN, bg=YELLOW)
Timer_label.grid(column=1,row=0)

checkmark_label = Label(fg= GREEN, bg=YELLOW)
checkmark_label.grid(column= 1,row=3)

startButton = Button(text="Start",command=start_timer, highlightthickness=0)
startButton.grid(column=0,row=2)

RestartButton = Button(text="Restart",command = reset_timer, highlightthickness=0)
RestartButton.grid(column=2,row=2)

window.mainloop()


#Dynamic Typing

#As soon as I sent a variable from a number to a string the type will also easily change
