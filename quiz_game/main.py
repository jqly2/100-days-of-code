from trivia import Trivia

quiz_session = Trivia()

for index in range(quiz_session.amount):
    current = quiz_session.new_question(index)
    quiz_session.check(index, current)
    
print(f"You have completed the quiz. \nYour final score is:{quiz_session.final_score()}")
    
    
    

        