# lets create a snake game
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# set up wizard completed

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

# snake body creation completed


is_game_on=True
snake=Snake()
food=Food()
scoreboard=ScoreBoard()
# now lets control snake with keywoed keys
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


# continously moving snake forward
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # new lets tackel the movement of snake
    # tail of the snake should follow the head of the tail
    # to achieve it we can move the segment 3 to segment 2 and segment 2 to segment 1 and head will move
    # segment 2 and 3 will follow the head

# lets detect the food
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend()
       scoreboard.increase_score()


# lets detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on=False
        scoreboard.game_over()

#    lets detect collision with tail first we need to extend the snake lets do it in snake class
    for positions in snake.segments[1:]:
        if snake.head.distance(positions)<10:
            is_game_on=False
            scoreboard.game_over()











screen.exitonclick()