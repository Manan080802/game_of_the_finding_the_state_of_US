import pandas as pd
import turtle
screen =turtle.Screen()
screen.title("U.S. State Game")
img= "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data=pd.read_csv("50_states.csv")
print(data)
all_states = data.state.to_list()
gussed_states=[]
while len(gussed_states)<50:
    answer_state = screen.textinput(title=f"{len(gussed_states)}/50Guess the state",prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not  in gussed_states:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        print(missing_state)
        break
    if answer_state in all_states:
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"]==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
