from trivia import Trivia

quiz_session = Trivia()

for index in range(quiz_session.amount):
    current = quiz_session.new_question(index)
    quiz_session.check(index, current)
    
    
    

        