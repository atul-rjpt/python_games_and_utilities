from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('gg sans', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.pu()
        self.setposition(0, 320)
        #self.shapesize(stretch_len=3, stretch_wid=3)
        self.score = 0
        self.update_score()
        
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font= FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font= FONT)
