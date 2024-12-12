import sys
import turtle
import Ball
import Player
import random
import heapq
import my_event
import dot
import keyboard
import time


class RunGame:
    def __init__(self, balls=5, dots=10):
        self.score = 0
        self.num_balls = balls
        self.ball_list = []
        self.num_dots = dots
        self.dots_lst = []
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        self.dt = 0.2
        turtle.hideturtle()
        turtle.speed(0)
        turtle.tracer(0)
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.player = Player.Player(self.canvas_width, self.canvas_height)
        print(self.canvas_width, self.canvas_height)
        self.ball_rad = int(0.1 * self.canvas_height)
        # adding ball to the list
        for i in range(self.num_balls):
            ball = Ball.Ball(self.ball_rad,
                             random.randint(-self.canvas_width + self.ball_rad, self.canvas_width - self.ball_rad),
                             random.randint(-self.canvas_height + self.ball_rad, self.canvas_height - self.ball_rad),
                             10 * self._random_no_0(), 10 * self._random_no_0(), i,
                             self.canvas_width, self.canvas_height)
            self.ball_list.append(ball)
        # adding dots
        for i in range(self.num_dots):
            d = dot.Dot(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                        random.randint(-self.canvas_height + 20, self.canvas_height - 20))
            self.dots_lst.append(d)

        self.ui = turtle.Turtle()
        self.ui.hideturtle()
        self.ui.penup()
        turtle.hideturtle()
        self.screen_ui = turtle.Screen()
        self.start = False

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
        for d in self.dots_lst:
            d.draw()
        for ball in self.ball_list:
            ball.draw()

    def in_game_ui(self):
        self.ui.color("black")
        self.ui.goto(200, 240)
        self.ui.write(f"Score: {self.score}", font=("Comic Sans MS", 30, "normal"))
        self.ui.goto(-350, 240)
        self.ui.color("DarkRed")
        self.ui.write(f"LIFE: {self.player.life}", font=("Comic Sans MS", 30, "normal"))

    def run(self):
        self.player.be_immune()  # let player be immune at the start
        self.player.body.showturtle()
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
            self.player.undash()

            for ball in self.ball_list:
                ball.move(self.dt)

            # check dot hit
            for d in self.dots_lst:
                if self.player.distance(d) <= (d.radius + 10):
                    self.score += 1
                    self.dots_lst.remove(d)
            # generate new dot
            if len(self.dots_lst) <= 8:
                d = dot.Dot(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                            random.randint(-self.canvas_height + 20, self.canvas_height - 20))
                self.dots_lst.append(d)
            # ball collision
            for ball in self.ball_list:
                ball.bounce_wall()
                # check hit player
                if (self.player.distance(ball) <= (ball.size + 10) and not self.player.immunity
                        and self.player.life > 0):
                    self.player.life -= 1
                    if self.player.life > 0:
                        self.player.be_immune()
                    if self.player.life == 0:
                        # stop the ball and player
                        self.player.disable_movement()
                        for b in self.ball_list:
                            b.moving = False
                        self.player.body.color("red")
                        break
                        # sys.exit()  # just close it
            turtle.clear()
            self.ui.clear()
            self.in_game_ui()
            self.__redraw()
            if self.player.life == 0:
                break
            self.player.stop_immune()

        print(f"score: {self.score}")

    def set_start(self):
        self.start = True

    def title_ui(self, color="green3"):
        turtle.hideturtle()
        self.ui.color("black")
        self.ui.goto(0, 50)
        self.ui.write("DOT DASH DODGE", font=("Courier", 50, "bold"), align="center")
        self.ui.goto(0, 0)
        self.ui.color(color)
        self.ui.write("press Space to Start", font=("Courier", 30, "bold"), align="center")

    def title(self):
        colorlst = ["green", "green3"]
        self.__draw_border()
        turtle.hideturtle()
        self.player.controlled()
        self.player.screen.listen()
        self.player.body.hideturtle()
        st = time.time()
        c = 0
        while True:
            if time.time() - st >= 0.5:
                st = time.time()
                if c == 0:
                    c = 1
                else:
                    c = 0
            turtle.clear()
            self.ui.clear()
            self.title_ui(colorlst[c])
            turtle.update()  # don't dare u remove this line this is life
            turtle.onkey(self.set_start, "space")
            if self.start:
                break
        self.ui.clear()
        self.run()


run = RunGame()
run.title()
# title not done yet run by run.run(
# run.run()
turtle.done()
