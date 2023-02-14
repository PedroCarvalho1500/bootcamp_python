from data import question_data
from question_model import Question
from quiz_brain import QuizBrain





if __name__ == '__main__':
    questions_objects = []
    for i in question_data: 
        question_text = i["question"]
        question_data = i["correct_answer"]
        #questions_objects.append(Question(i))
        questions_objects.append(Question(question_text, question_data))
    
    
    new_quiz_brain = QuizBrain(questions_objects)

    while(new_quiz_brain.still_has_questions() == True):
        new_quiz_brain.next_question()

    print(f'You have completed the quiz\nYour final score was: {new_quiz_brain.score}/{len(new_quiz_brain.question_list)} ')