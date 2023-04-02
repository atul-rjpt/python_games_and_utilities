from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for _ in range(3):
            x = -20
            y = 0
            position = (x, y)
            self.add_segment(position)
            x -= 20

    def add_segment(self, position):
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setposition(position)
            self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0, -1):
            dest = self.segments[seg_num-1].position()
            self.segments[seg_num].goto(dest)
        self.head.forward(20)

    def up(self): 
        if self.head.heading() != DOWN:       
            self.head.setheading(UP)
        # self.move()

    def down(self):
        if self.head.heading() != UP:   
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)

    def right(self): 
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

