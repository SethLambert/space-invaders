from turtle import Turtle,register_shape

class HeroLaser(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        shape = ((-1,10),(-1,-10),(1,10),(1,-10))
        register_shape('hero-laser', shape)
        self.shape('hero-laser')
        self.penup()
        self.right(90)
        self.y_move = 10
        self.move_speed = 0.1
        self.goto(self.xcor(),-260)
        self.moving = False
        
    def fire(self):
        new_x = self.xcor()
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.moving = True
        
    def move(self, ship_x):
        if self.moving == True:
            new_x = self.xcor()
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        else:
            self.goto(ship_x,-260)
        if self.ycor() > 300:
            self.moving = False
            self.goto(ship_x,-260)
    
    def hit(self, ship_x):
        self.moving = False
        self.goto(ship_x,-260)
        