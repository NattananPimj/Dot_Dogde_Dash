import turtle
import math


class Ball:
    def __init__(self, size: int, x: float, y: float, vx: float, vy: float, width: float, height: float):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = "red"
        self.count = 0
        self.canvas_width = width
        self.canvas_height = height
        self.moving = True
        turtle.hideturtle()

    def draw(self):
        # draw a circle of radius equals to size centered at (x, y) and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    # def bounce_off_vertical_wall(self):
    #     self.vx = -self.vx
    #     self.count += 1
    #
    # def bounce_off_horizontal_wall(self):
    #     self.vy = -self.vy
    #     self.count += 1

    def bounce_wall(self):
        if self.x >= self.canvas_width - self.size or self.x <= -self.canvas_width + self.size:
            self.vx = -self.vx
        if self.y >= self.canvas_height - self.size or self.y <= -self.canvas_height + self.size:
            self.vy = -self.vy

    def bounce_off(self, that):
        dx = that.x - self.x
        dy = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx * dvx + dy * dvy  # dv dot dr
        dist = self.size + that.size  # distance between particle centers at collison

        # magnitude of normal force
        magnitude = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)

        # normal force, and in x and y directions
        fx = magnitude * dx / dist
        fy = magnitude * dy / dist

        # update velocities according to normal force
        self.vx += fx / self.mass
        self.vy += fy / self.mass
        that.vx -= fx / that.mass
        that.vy -= fy / that.mass

        # update collision counts
        self.count += 1
        that.count += 1

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
