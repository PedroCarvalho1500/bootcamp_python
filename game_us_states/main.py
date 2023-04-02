import pandas as pd
import turtle


# def get_mouse_click_coor(x,y):
#     print(x,y)


def create_csv_missed_states(guessed, states, missed):
    for state in states:
        if state not in guessed:
            missed["States"].append(state)
    
    df = pd.DataFrame(missed)
    df.to_csv("states_to_learn.csv")
    


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.setup(width=800, height=600)
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    data = pd.read_csv('50_states.csv')
    states = data["state"].to_list()
    
    missed_states_dict = {"States": []}
    
    guessed_states = []
    
    game_finish = False
    
    while(len(guessed_states) < 50):
        
        try:
            answer_state = (screen.textinput(title="Guess the state", prompt="What's another state's name?r")).title()
        except:
            create_csv_missed_states(guessed_states, states, missed_states_dict)
            exit()
        

        
        #coords_answer = coords_state["x"],coords_state["y"]
        
        
        #print(f"X AND Y COORDINATES FOR {answer_state}: {}")
        
        #print(states)

        if(answer_state in states):
            guessed_states.append(answer_state)
            coords_state = data[data["state"] == answer_state]
            print("MATCH")
            t = turtle.Turtle()
            t.hideturtle()
            t.color('black')
            t.penup()
            t.goto(int(coords_state.x),int(coords_state.y))
            t.write(answer_state, align="center", font=("Courier", 10, "bold"))  


    screen.mainloop()
    #screen.exitonclick()