import sys
import turtle
import Ball
import Player
import random
import heapq
import my_event
import dot


class RunGame:
    def __init__(self, balls=5, dots=10):
        self.score = 0
        self.num_balls = balls
        self.ball_list = []
        self.num_dots = dots
        self.dos_lst = []
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        self.dt = 0.2
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
                             10 * self._random_no_0(), 10 * self._random_no_0(), i,
                             self.canvas_width, self.canvas_height)
            self.ball_list.append(ball)
        for i in range(self.num_dots):
            d = dot.Dot(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                        random.randint(-self.canvas_height + 20, self.canvas_height - 20))
            self.dos_lst.append(d)
        self.player.be_immune()
        self.ui = turtle.Turtle()
        self.ui.hideturtle()
        self.ui.penup()

    def _random_no_0(self):
        while True:
            value = random.uniform(-1, 1)
            if value != 0:
                return value

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

    def _draw_ui(self):
        self.ui.color("black")
        self.ui.goto(200, 240)
        self.ui.write(f"Score: {self.score}", font=("Comic Sans MS", 30, "normal"))
        self.ui.goto(-350, 240)
        self.ui.color("DarkRed")
        self.ui.write(f"LIFE: {self.player.life}", font=("Comic Sans MS", 30, "normal"))

    def run(self):
        self.__draw_border()
        turtle.hideturtle()
        for ball in self.ball_list:
            ball.draw()

        self.player.controlled()
        self.player.screen.listen()

        while True:
            self._draw_ui()
            self.player.check_wall()
            self.player.body.showturtle()
            self.player.movement()
            self.player.undash()

            for ball in self.ball_list:
                ball.move(self.dt)

            # check hit
            for d in self.dos_lst:
                if self.player.distance(d) <= (d.radius + 10):
                    self.score += 1
                    self.dos_lst.remove(d)
            if len(self.dos_lst) <= 8:
                d = dot.Dot(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                            random.randint(-self.canvas_height + 20, self.canvas_height - 20))
                self.dos_lst.append(d)
            # ball collision
            for ball in self.ball_list:
                ball.bounce_wall()
                # check hit player
                if (self.player.distance(ball) <= (ball.size + 10) and not self.player.immunity
                        and self.player.life > 0):
                    self.player.life -= 1
                    print(self.player.life)
                    if self.player.life > 0:
                        self.player.be_immune()
                    if self.player.life == 0:
                        print(f"score: {self.score}")
                        self.player.disable_movement()
                        self.player.body.color("red")
                        # sys.exit()  # just close it
            self.player.stop_immune()

            turtle.clear()
            self.ui.clear()
            self.__redraw()


run = RunGame()
run.run()
turtle.done()
