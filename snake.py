
from turtle import Turtle
DISTANCIA = 20
POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

        
class Snake():
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    #creando una array de Turtle( con posicion )    
    def add_segment(self, position ):
        seg = Turtle('square')
        seg.shape("square")
        seg.color('white')
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)
        
    def create_snake(self):
        for pos in POSITION:
            self.add_segment(pos)
    def extend(self):
        self.add_segment(self.segments[-1].position())
            
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.head.forward(DISTANCIA)
        
    #cambiar de direcion    
    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)
    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)