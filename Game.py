import turtle
import Ball
import Player
import random
import heapq
import my_event
import dot


class RunGame:
    def __init__(self, balls=5, dots=10):
        self.num_balls = balls
        self.ball_list = []
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
        self.ball_rad = int(0.1 * self.canvas_height)
        for i in range(self.num_balls):
            ball = Ball.Ball(self.ball_rad,
                             random.randint(-self.canvas_width + self.ball_rad, self.canvas_width - self.ball_rad),
                             random.randint(-self.canvas_height + self.ball_rad, self.canvas_height - self.ball_rad),
                             random.randint(-10, 10), random.randint(-10, 10), i,
                             self.canvas_width, self.canvas_height)
            self.ball_list.append(ball)
        for i in range(self.num_dots):
            d = dot.Dot(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                        random.randint(-self.canvas_height + 20, self.canvas_height - 20))
            self.dos_lst.append(d)

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

    def __redraw(self):
        self.__draw_border()
        for d in self.dos_lst:
            d.draw()
        for ball in self.ball_list:
            ball.draw()

    def run(self):

        self.__draw_border()
        turtle.hideturtle()
        for ball in self.ball_list:
            ball.draw()

        self.player.controlled()
        self.player.screen.listen()

        while True:
            self.player.check_wall()
            self.player.body.showturtle()
            self.player.movement()
            for ball in self.ball_list:
                ball.move(0.01)
            for d in self.dos_lst:
                if self.player.distance(d) <= (d.radius + 10):
                    self.player.score += 1
                    self.dos_lst.remove(d)
            if len(self.dos_lst) <= 8:
                d = dot.Dot(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                            random.randint(-self.canvas_height + 20, self.canvas_height - 20))
                self.dos_lst.append(d)
            turtle.clear()
            self.__redraw()


run = RunGame()
run.run()
turtle.done()
