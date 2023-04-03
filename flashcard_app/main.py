from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


def generate_random_french_word(dictionary):
    french, english = random.choice(list(dictionary.items()))

    print(french, english)

    return french
    

def generate_random_english_word(dictionary):
    french, english = random.choice(list(dictionary.items()))

    print(french, english)

    return english


def update_front_card(canvas):
    canvas.itemconfig(canvas_front_text, text=generate_random_french_word(words_dict))

if __name__ == '__main__':
    window = Tk()
    window.title("FlashCard APP")
    window.config(padx=100, pady=100, background=BACKGROUND_COLOR, height=528, width=800)
    window.resizable(False,False)

    data_words = pandas.read_csv("data/french_words.csv")

    words_dict = {row.French: row.English for (index, row) in data_words.iterrows()}
    #print(words_dict)


    flashcard_canvas_front = Canvas(width=800, height=518, background=BACKGROUND_COLOR, highlightthickness=0)
    my_flashcard_front_image = PhotoImage(file="images/card_front.png")
    flashcard_canvas_front.create_image(400,270,image=my_flashcard_front_image)
    canvas_front_text = flashcard_canvas_front.create_text(400,263,text=generate_random_french_word(words_dict),font=("Arial", 60, 'bold'))
    canvas_front_language = flashcard_canvas_front.create_text(400,150,text="French",font=("Arial", 40, 'italic'))
    flashcard_canvas_front.grid(column=1, row=1, columnspan=2)



    right_image = PhotoImage(file="images/right.png")
    button_right = Button(image=right_image, highlightthickness=0, command=lambda: update_front_card(flashcard_canvas_front))
    button_right.grid(column=2, row=2, pady=50, padx=50)


    left_image = PhotoImage(file="images/wrong.png")
    button_left = Button(image=left_image, highlightthickness=0, command=lambda: update_front_card(flashcard_canvas_front))
    button_left.grid(column=1, row=2, pady=50, padx=50)

    window.mainloop()