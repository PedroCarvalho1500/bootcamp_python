THEME_COLOR = "#375362"
ALIGNMENT = "center"
FONT = ("Arial", 20, "italic")

import time
from tkinter import *
import quiz_brain

class ScreenFunctions():
    def __init__(self):
        pass

    def canvas_green(self):
        self.canvas_quiz.configure(bg='green')
        time.sleep(1)

        #self.canvas_quiz.configure(bg="gray100")
        #self.canvas_quiz.after_cancel(self.canvas_quiz)
        
    def lost_game_feedback(self):
        self.canvas_quiz.configure(bg='gray100')
        self.canvas_quiz.itemconfig(self.canvas_text, text="You Lost the Game!")
        self.main_window.after_cancel(self.loop_main_window)

    def give_feedback(self, is_right):
        
        if(is_right): 
            self.canvas_quiz.configure(bg='green')
            self.loop_main_window = self.main_window.after(1000, self.get_next_question)
            #time.sleep(1)
            #self.canvas_quiz.configure(bg='green')
            
        else: 
            self.canvas_quiz.configure(bg='red')
            self.loop_main_window = self.main_window.after(1000, self.lost_game_feedback)
            
            #time.sleep(1)
            
        #time.sleep(3)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas_quiz.configure(bg='gray100')
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")

            q_text = self.quiz.next_question()
            self.canvas_quiz.itemconfig(self.canvas_text, text=q_text)
            self.main_window.after_cancel(self.loop_main_window)

        else:
            self.canvas_quiz.configure(bg='gray100')
            self.canvas_quiz.itemconfig(self.canvas_text, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.main_window.after_cancel(self.loop_main_window)


    def check_answer_ui(self, answer):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        if(self.quiz.check_answer(answer) == True): 
            #print(f"Your current score is: {self.score}/{self.question_number}")
            self.give_feedback(True)
            self.score+=1
            self.score_label.config(text="Score: "+str(self.score))
            
        else: 
            self.give_feedback(False)
            


        
class QuizInterface(ScreenFunctions):
    def __init__(self, main_window, quiz_brain):
        self.main_window = main_window
        self.loop_main_window = self.main_window.after(1000, self.get_next_question)
        self.quiz = quiz_brain
        self.score = 0

        #input(f"QUIZ BRAIN: {str(self.quiz)}")

        self.main_window.title("Quizzler")
        self.main_window.geometry("340x500")

        self.main_window.config(background=THEME_COLOR)

        self.canvas()
        self.label()
        self.buttons()
        self.get_next_question()
        #canvas = Canvas(width=300, height=414)
        # background_img = PhotoImage(file="background.png")
        # canvas.create_image(150, 207, image=background_img)
        # quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
        # canvas.grid(row=0, column=0)

        # kanye_img = PhotoImage(file="kanye.png")
        # kanye_button = Button(image=kanye_img, highlightthickness=0, command=lambda: get_quote(canvas))
        # kanye_button.grid(row=1, column=0)


        self.main_window.mainloop()


    def canvas(self):
        self.canvas_quiz = Canvas(width=300, height=250, bg='gray100')
        self.canvas_quiz.grid(row=1, column=0, columnspan=2, rowspan=1, padx=20, pady=20)
        self.canvas_text = self.canvas_quiz.create_text(150,125,text="", font=FONT, fill=THEME_COLOR, width=270)

    def label(self):
        self.score_label = Label(text="Score: "+str(self.score), bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

    def buttons(self):
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=lambda: self.check_answer_ui("True"))
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=lambda: self.check_answer_ui("False"))
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

if __name__ == '__main__':
    main_window = Tk()
    QuizInterface(main_window)