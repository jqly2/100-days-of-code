class Score:
    def __init__(self) -> None:
        self.score = 0
    
    def update(self):
        self.score += 1
    
    def display(self, index):
        return print(f"Your current score is: {self.score}/{index+1}.")
    
    def final(self):
        return self.score