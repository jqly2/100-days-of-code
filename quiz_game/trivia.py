
from score import Score
import data
import requests
import json

api_url = "https://opentdb.com/api.php?amount=40&type=boolean"

response = requests.get(api_url)
if response.status_code == 200:
    current_api_session = json.loads(response.text)
score_sesssion = Score()

class Trivia:
    def __init__(self):
        if current_api_session['response_code'] == 0:
            self.questions = current_api_session['results']
            self.amount = len(current_api_session["results"])
        else:
            print(response.status_code)
            self.questions = data.question_data
            self.amount = len(data.question_data)
    
    def check(self, number ,answer):
        if answer == "true" or answer == "t":
            answer = "true"
        else:
            answer = "false"
        if self.questions[number]["correct_answer"].lower() == answer:
            score_sesssion.update()
            print(f"You got it right!\nThe correct answer was:{self.questions[number]['correct_answer'].capitalize()}")
            return score_sesssion.display(number) 
        else:
            print(f"That's wrong. \nThe correct answer was:{self.questions[number]['correct_answer'].capitalize()}")
            return score_sesssion.display(number)
        
    def new_question(self, number):
        return input(f"Q.{number+1} {self.questions[number]['question']} (True/False)?:")