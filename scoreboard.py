from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 265)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.UptadeScore()
    
    def UptadeScore(self):
        self.write(f"score: {self.score}", align = ALIGNMENT, font = FONT)
        
    def Game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align = ALIGNMENT, font = FONT)
        
    
    def IncreaseScore(self):
        self.score += 1
        self.clear()
        self.UptadeScore()
        
        