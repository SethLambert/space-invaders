from turtle import Turtle,register_shape
import random

start_x = [180,160,140,120,100,80,60,40,20,0,-20,-40,-60,-80,-100,-120,-140,-160,-180]

class EnemyBomb(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        register_shape('assets\enemy-bomb.gif')
        self.shape('assets\enemy-bomb.gif')
        self.penup()
        self.right(90)
        self.x = random.choice(start_x)
        self.y_move = -10
        self.move_speed = 0.1
        self.goto(self.x,500)
        self.moving = False
        
    def fire(self):
        new_x = self.xcor()
        new_y = 100
        self.goto(new_x, new_y)
        self.moving = True
        
    def move(self):
        if self.moving == True:
            new_x = self.xcor()
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        else:
            self.goto(self.x,500)
        if self.ycor() > 300:
            self.moving = False
            self.goto(self.x, 500)
    
    def hit(self):
        self.moving = False
        self.goto(self.x,500)