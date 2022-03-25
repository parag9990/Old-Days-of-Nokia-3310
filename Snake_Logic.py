from turtle import *
import time
import random as r
directions = {'Up':90, 'Down':270, 'Left':180,'Right':0}
start_POS = [(0, 0),(-20, 0),(-40, 0)]
try:
    class Snake:

        def __init__(self):
            # Create Snake
            self.all_turtles = []
            self.create_Snake()
            self.front = self.all_turtles[0]

        def create_Snake(self):
            for tu in start_POS:
                self.Turtle_add(tu)
                
        def Turtle_add(self, tu):
            tim = Turtle(shape='square')
            tim.color('white')
            tim.penup()
            tim.goto(tu)
            self.all_turtles.append(tim)

        def tail(self):
            self.Turtle_add(self.all_turtles[-1].position())

        def move(self):
            for i in range(len(self.all_turtles) - 1, 0, -1):
                # print(i)
                x_cordinate = self.all_turtles[i - 1].xcor()
                y_cordinate = self.all_turtles[i - 1].ycor()
                self.all_turtles[i].goto(x_cordinate, y_cordinate)
            self.front.forward(20)

        def up(self):
            if self.front.heading()!=directions['Down']:
                self.front.setheading(directions['Up'])

        def down(self):
            if self.front.heading()!=directions['Up']:
                self.front.setheading(directions['Down'])

        def left(self):
            if self.front.heading()!=directions['Right']:
                self.front.setheading(directions['Left'])

        def right(self):
            if self.front.heading()!=directions['Left']:
                self.front.setheading(directions['Right'])

except:
    print('This is Class for the Snake Game.')


# Random Food Items Class

try:
    class Food(Turtle):
        def __init__(self):
            super().__init__()
            self.shape('circle')
            self.penup()
            self.shapesize(stretch_len=0.5,stretch_wid=0.5)
            self.color('red')
            self.speed('fastest')
            self.create_food()

        
        def create_food(self):
            x_axis = r.randint(-250, 250)
            y_axis = r.randint(-250, 250)
            self.goto(x_axis, y_axis)
            
except:
    print('The Food class is not Working.')


# ScoreBoard Class

try:
    class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.color('white')
            self.penup()
            self.goto(0, 260)
            self.hideturtle()
            self.update_score()


        def update_score(self):
            self.write(f'Score = {self.score}', align='center',font=('Merriweather', 20, 'normal'))

        def increment(self):
            self.score += 1
            self.clear()
            self.update_score()
            
        def game_end(self):
            self.goto(0, 0)
            self.write('GAME OVER 💀', align='center',font=('Merriweather', 20, 'normal'))

except:
    print('The Scoreboard Class is not Working.')