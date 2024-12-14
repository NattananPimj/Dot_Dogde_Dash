import turtle
import math
import dot


class Ball(dot.Dot):
    def __init__(self, size: int, x: float, y: float, vx: float, vy: float, width: float, height: float):
        super().__init__(x, y)
        self.radius = size
        self.vx = vx
        self.vy = vy
        self.color = "red"
        self.canvas_width = width
        self.canvas_height = height
        self.moving = True
        turtle.pensize(5)

    def bounce_wall(self):
        if self.x >= self.canvas_width - self.radius or self.x <= -self.canvas_width + self.radius:
            self.vx = -self.vx
        if self.y >= self.canvas_height - self.radius or self.y <= -self.canvas_height + self.radius:
            self.vy = -self.vy

    def distance(self, that):
        x1 = self.x
        y1 = self.y
        x2 = that.x
        y2 = that.y
        d = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return d

    def move(self, dt):
        if self.moving:
            self.x += self.vx * dt
            self.y += self.vy * dt
