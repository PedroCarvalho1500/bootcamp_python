import time
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_french_word = ""

time_passed = 0
data_words = pandas.read_csv("data/french_words.csv")
to_learn = data_words.to_dict(orient="records")
words_to_learn_data = ""
words_to_learn_dict_list = to_learn


def generate_random_french_word():
    global current_french_word, words_to_learn_data, words_to_learn_dict_list
    #current_french_word = random.choice(to_learn)
    #return current_french_word["French"]
    try:
        words_to_learn_data = pandas.read_csv("data/words_to_learn.csv")
        words_to_learn_dict_list = words_to_learn_data.to_dict(orient="records")
        current_french_word = random.choice(words_to_learn_dict_list)
        return current_french_word["French"]

    except FileNotFoundError:
        df = pandas.DataFrame(to_learn)
        df.to_csv('data/words_to_learn.csv', index=False)
        current_french_word = random.choice(to_learn)
        return current_french_word["French"] 

    except IndexError:
        #file = open("data/words_to_learn.csv", mode="w")
        current_french_word = random.choice(to_learn)
        return current_french_word["French"]



def get_the_english_word():
    global current_french_word
    return current_french_word["English"]

    
def is_known():
    global words_to_learn_dict_list, current_french_word
    words_to_learn_dict_list.remove(current_french_word)


def update_words_to_learn_csv():
    global words_to_learn_dict_list
    #print(len(words_to_learn_dict_list))
    df = pandas.DataFrame(words_to_learn_dict_list)
    df.to_csv('data/words_to_learn.csv', index=False)


def update_front_card(canvas):
    canvas.itemconfig(canvas_text, text=generate_random_french_word())


def change_to_back_card(canvas, window, new_image):
    canvas.itemconfig(image_front, image=new_image)
    canvas.itemconfig(canvas_text, text=get_the_english_word())
    canvas.itemconfig(canvas_language, text="English",font=("Arial", 40, 'italic'))
    window.after_cancel(window)

def change_to_front_card(canvas, window, old_image, miss=0):
    global words_to_learn_data, words_to_learn_dict_list, current_french_word

    if(miss == 1):
        #input(f'{words_to_learn_dict_list}')
        if current_french_word not in words_to_learn_dict_list:
            df = pandas.DataFrame({"French": [current_french_word["French"]], "English": [current_french_word["English"]]})
            df.to_csv('data/words_to_learn.csv', mode='a', index=False, header=False)
        window.after_cancel(window)
        canvas.itemconfig(image_front, image=old_image)
        canvas.itemconfig(canvas_text, text=generate_random_french_word())
        canvas.itemconfig(canvas_language, text="French",font=("Arial", 40, 'italic'))
        window.after(3000, change_to_back_card, flashcard_canvas, window, new_image)

    else:
        is_known()
        update_words_to_learn_csv()

        window.after_cancel(window)
        canvas.itemconfig(image_front, image=old_image)
        canvas.itemconfig(canvas_text, text=generate_random_french_word())
        canvas.itemconfig(canvas_language, text="French",font=("Arial", 40, 'italic'))
        window.after(3000, change_to_back_card, flashcard_canvas, window, new_image)



if __name__ == '__main__':
    window = Tk()
    window.title("FlashCard APP")
    window.config(padx=100, pady=100, background=BACKGROUND_COLOR, height=528, width=800)
    window.resizable(False,False)


    #print(to_learn)
    #data_frame = pandas.DataFrame.to_dict(data_words, orient="records")


    #print(data_frame)
    words_dict = {row.French: row.English for (index, row) in data_words.iterrows()}
    
    
    

    flashcard_canvas = Canvas(width=800, height=518, background=BACKGROUND_COLOR, highlightthickness=0)
    my_flashcard_image = PhotoImage(file="images/card_front.png")
    new_image = PhotoImage(file="images/card_back.png")

    image_front = flashcard_canvas.create_image(400,270,image=my_flashcard_image)
    canvas_text = flashcard_canvas.create_text(400,263,text=generate_random_french_word(),font=("Arial", 60, 'bold'))
    canvas_language = flashcard_canvas.create_text(400,150,text="French",font=("Arial", 40, 'italic'))
    flashcard_canvas.grid(column=1, row=1, columnspan=2)



    right_image = PhotoImage(file="images/right.png")
    button_right = Button(image=right_image, highlightthickness=0, command=lambda: change_to_front_card(flashcard_canvas, window, my_flashcard_image, 0))
    button_right.grid(column=2, row=2, pady=50, padx=50)


    left_image = PhotoImage(file="images/wrong.png")
    button_left = Button(image=left_image, highlightthickness=0, command=lambda: change_to_front_card(flashcard_canvas, window, my_flashcard_image, 1))
    button_left.grid(column=1, row=2, pady=50, padx=50)

    window.after(3000, change_to_back_card, flashcard_canvas, window, new_image)
    window.mainloop()