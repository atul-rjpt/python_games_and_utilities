from turtle import Turtle
import random

FOOD_SHAPE = 'turtle'
FOOD_COLOR = 'green'

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        # self.hideturtle()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color(FOOD_COLOR)
        self.penup()
        #self.write('🍎')
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        random_x = random.randrange(-260, 260, 20)
        random_y = random.randrange(-260, 260, 20)
        self.setposition(random_x, random_y)
        
