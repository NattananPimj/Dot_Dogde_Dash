import turtle


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'blue'
        self.radius = 2

    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
