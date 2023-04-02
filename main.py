from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from walls import Wall
import time

# Creating Objects
screen = Screen()
screen.setup(width=700, height=750)
wall = Wall()
scoreboard = Scoreboard()
snake = Snake()
food = Food()


# Screen Setup
screen.title('Snake World')
screen.bgcolor('#212121')
screen.tracer(0)

# Key Commands
screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
# Collision With the WaLL
    if x_cor >= 290:
        snake.head.goto(-280, y_cor)
    elif x_cor <= -290:
        snake.head.goto(280, y_cor)
    elif y_cor >= 290:
        snake.head.goto(x_cor, -280)
    elif y_cor <= -290: 
        snake.head.goto(x_cor, 280)

        #scoreboard.game_over()
# Collision with the Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
