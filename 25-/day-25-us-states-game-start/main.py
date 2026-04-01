import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/52 states guessed", prompt = "What's another state's name?" ).title()

    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in guessed_states]
        to_learn = pandas.DataFrame(states_to_learn)
        to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        answer= data[data.state == answer_state]
        x_cor = answer["x"].item() #this item() was the bug I was trying to fix,
        # The error i was getting was bad screen distance,
        # type(y_cor) was returning two number the index of columns and the y coord,
        # the item() method accesses the single item in the panda Series
        y_cor = answer["y"].item()
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(x_cor, y_cor)
        text.write(f"{answer_state}", False, "center", ("Arial", 8, "normal"))
