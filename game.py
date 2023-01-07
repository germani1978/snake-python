import time
from turtle import Turtle, Screen
from food import Food
from scoreboard import Score
from snake import Snake

DIST = 280

screen = Screen()
def init():
    screen.bgcolor('black')
    screen.setup( width= 600, height=600)
    screen.tracer(0)
init()

#crear la serpiente
snake = Snake()

#crear la comida
food = Food()
score = Score()

#mover la serpiente
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detecta si choca con la comida
    if snake.head.distance(food)<15:
        food.refresh_pos()
        snake.extend()
        score.increment_score()
        
    #detecta si choca con las paredes    
    print(snake.head.ycor())
    if snake.head.xcor() > DIST or snake.head.xcor() < -DIST-20 or snake.head.ycor() > DIST + 20 or snake.head.ycor() < -DIST-20 : 
        game_on = False
        score.game_over()


    #acabar si choca con el mismo
    for seg in snake.segments[1:]:
        if  seg.distance(snake.head) < 10 :
            game_on = False
            score.game_over()
            
           

screen.exitonclick()
