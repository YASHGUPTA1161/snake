from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
# speed = float(screen.textinput(title="mode", prompt="pick speed"))

screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()     
food = Food()   
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")    
screen.onkey(snake.down, "Down")    
screen.onkey(snake.left, "Left")    
screen.onkey(snake.right, "Right")    

game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(speed)
    time.sleep(0.2)
    snake.move()
    
# detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        # snake.snake_color()
        snake.extend()
        scoreboard.IncreaseScore()
# detect collision
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False 
        scoreboard.Game_over()
# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False 
            scoreboard.Game_over()
            
    
screen.exitonclick()
