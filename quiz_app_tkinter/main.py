from tkinter import Tk
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []


# while quiz.still_has_questions():
#     quiz.next_question()


if __name__ == '__main__':
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)





    quiz = QuizBrain(question_bank)
    quiz_screen_ui = Tk()

    quiz_ui = QuizInterface(quiz_screen_ui, quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
