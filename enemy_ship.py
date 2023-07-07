from turtle import Turtle, register_shape

class EnemyShip(Turtle):
    
    def __init__(self, position, color = "red"):
        super().__init__()
        shape = (
            (1,3),(3,1),(8,6),(10,4),(12,6),(17,1),(19,3),(17,5),(17,7),(20,10),(20,15),(15,20),
            (12,17),(14,15),(12,13),(10,15),(8,13),(6,15),(8,17),(5,20),(0,15),(0,10),(3,7),(3,5)
        )
        register_shape('alien-ship', shape)
        self.shape('alien-ship')
        self.color(color)
        self.right(90)
        self.shapesize(stretch_wid=1, stretch_len=1) 
        self.penup()
        self.goto(position)
        self.strafe = 10
    
    def destroy(self):
        self.goto(-1000,-1000)
        
    def move(self):
        if self.ycor() % 10 == 0:
            self.strafe *= -1
            new_x = self.xcor() + self.strafe
        else:
            new_x = self.xcor()
        new_y = self.ycor() - 1
        self.goto(new_x, new_y)