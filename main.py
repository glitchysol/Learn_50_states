import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
game_is_on = True

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
x_list = states.x.to_list()
y_list = states.y.to_list()
states_correct = []


answer_state = screen.textinput(title="Guess the State", prompt="Can you name a state?")
answer_state = answer_state.title()


def add_state():
    position = states_list.index(answer_state)
    location = (x_list[position], y_list[position])
    new_state = turtle.Turtle()
    new_state.up()
    new_state.ht()
    new_state.goto(location)
    new_state.write(answer_state)
    states_correct.append(answer_state)

    
add_state()

while game_is_on:
    answer_state = screen.textinput(title=f"{len(states_correct)}/50 States Correct", prompt="What's another state name?")
    answer_state = answer_state.title()
    if answer_state in states_list:
        add_state()
    else:
        continue

screen.mainloop()





