import turtle


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'green'
        self.radius = 0.2
        turtle.pensize(1)
        turtle.hideturtle()

    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
