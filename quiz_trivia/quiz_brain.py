#TODO asking the questions
#TODO checking if the answer was correct
#TODO checking if we're the end of the quiz


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        #print(f'{self.question_list[0].answer}')
        
    def next_question(self):
        #hit_answer = True
        #current_question = self.question_list[self.question_number]
        
        player_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)? ")
        
        if(self.check_question_answer(self.question_list[self.question_number], player_answer)): 
            self.question_number+=1
            self.score += 1
            print(f'Your current score is {self.question_number}/{self.score}')
            
        else:
            print(f"You Lost The Game!!! The correct answer was {self.question_list[self.question_number].answer}")
            self.question_number = len(self.question_list)
            
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    
    def check_question_answer(self, question, answer):
        return question.answer.lower() == answer.lower()