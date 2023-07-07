from turtle import Turtle, register_shape

class HomeBase(Turtle):
    
    def __init__(self, position):
        super().__init__()
        register_shape('assets\home-base.gif')
        self.shape('assets\home-base.gif')
        self.penup()
        self.goto(position)
        
    def hit(self):
        register_shape('assets\ship-destroyed.gif')
        self.shape('assets\ship-destroyed.gif')
        self.goto(-1000,-1000)