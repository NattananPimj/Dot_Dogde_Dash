import turtle
import Ball
import math
import Player
import random


class RunGame:
    def __init__(self, balls=5, dots=5):
        self.num_balls = balls
        self.balls_lst = []
        self.num_dots = dots
        self.dos_lst = []
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.player = Player.Player(self.canvas_width, self.canvas_height)
        print(self.canvas_width, self.canvas_height)
        self.ball_rad = int(0.05 * self.canvas_height)
        for i in range(self.num_balls):
            ball = Ball.Ball(self.ball_rad,
                             random.randint(-self.canvas_width + self.ball_rad, self.canvas_width - self.ball_rad),
                             random.randint(-self.canvas_height + self.ball_rad, self.canvas_height - self.ball_rad),
                             1, 1, 1,
                             self.canvas_width, self.canvas_height)
            self.balls_lst.append(ball)

    def __draw_border(self):
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def run(self):
        self.__draw_border()
        turtle.hideturtle()
        for ball in self.balls_lst:
            ball.draw()

        self.player.controlled()
        self.player.screen.listen()

        while True:
            self.player.check_wall()
            self.player.body.showturtle()
            self.player.movement()
            for ball in self.balls_lst:
                ball.move(0.01)
            turtle.clear()
            self.__draw_border()
            for ball in self.balls_lst:
                ball.draw()


run = RunGame()
run.run()
turtle.done()
