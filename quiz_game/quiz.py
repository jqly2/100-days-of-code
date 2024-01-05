import data
from score import Score

score_sesssion = Score()

class Quiz:
    def __init__(self):
        self.questions = data.question_data
        self.amount = len(data.question_data)
    
    def check(self, number ,answer):
        if answer == "true" or answer == "t":
            answer = "true"
        else:
            answer = "false"
        if self.questions[number]["correct_answer"].lower() == answer:
            score_sesssion.update()
            print(f"You got it right!\nThe correct answer was:{answer.capitalize()}")
            return score_sesssion.display(number) 
        else:
            print(f"That's wrong. \nThe correct answer was:{answer.capitalize()}")
            return score_sesssion.display(number)
        
    def new_question(self, number):
        return input(f"Q.{number+1} {self.questions[number]['question']} (True/False)?:")
    
    def final_score(self):
        return f"{score_sesssion.final()}/{self.amount}"