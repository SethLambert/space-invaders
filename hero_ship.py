from turtle import Turtle, register_shape

class HeroShip(Turtle):
    
    def __init__(self, position):
        super().__init__()
        register_shape('assets\hero-ship.gif')
        self.shape('assets\hero-ship.gif')
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5) 
        self.penup()
        self.goto(position)
        
    def go_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
    
    def go_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())
        
    def hit(self):
        register_shape('assets\ship-destroyed.gif')
        self.shape('assets\ship-destroyed.gif')