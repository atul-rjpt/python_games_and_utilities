from turtle import Turtle

X_COR = 300
Y_COR = 300

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.penup()
        self.goto(-X_COR, Y_COR)
        self.pendown()
        self.goto(-X_COR, -Y_COR)
        self.goto(X_COR, -Y_COR)
        self.goto(X_COR, Y_COR)
        self.goto(-X_COR, Y_COR)
