from turtle import Turtle, Screen
from Snake_Logic import Scoreboard, Snake, Food
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Nokia 3310 Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
Score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')


game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # For Food
    if snake.front.distance(food) < 15:
        food.create_food()
        snake.tail()
        Score.increment()

    # For Wall
    if snake.front.xcor() > 282 or snake.front.xcor() < -282 or snake.front.ycor() > 282 or snake.front.ycor() < -282:
        game = False
        Score.game_end()

    # For Tail
    for tur in snake.all_turtles:
        if tur == snake.front:
            pass
        elif snake.front.distance(tur) < 10:
            game = False
            Score.game_end()
screen.exitonclick()
