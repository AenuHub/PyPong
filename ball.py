from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = MOVE_DISTANCE
        self.y = MOVE_DISTANCE
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self, ):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()