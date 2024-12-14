import turtle
import Ball
import Player
import random
import dot
import time


def _random_no_0():
    while True:
        value = random.uniform(-1, 1)
        if value != 0:
            return value


class RunGame:
    def __init__(self, balls=5, dots=10, size=0.1,
                 speed=10, player_speed: float = 0.8, score_diff=50, score_lst=None):
        self.speed = speed
        if score_lst is None:
            score_lst = [0]
        self.__score = 0
        self.__score_lst = score_lst
        self.num_balls = balls
        self.ball_list = []
        self.num_dots = dots
        self.dots_lst = []
        self.dt = 0.2
        turtle.hideturtle()
        turtle.speed(0)
        turtle.tracer(0)
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.player_speed = player_speed
        self.player = Player.Player(self.canvas_width, self.canvas_height, self.player_speed)
        print(self.canvas_width, self.canvas_height)
        self.size = size
        self.ball_rad = int(self.size * self.canvas_height)
        # adding ball to the list
        for i in range(self.num_balls):
            ball = Ball.Ball(self.ball_rad,
                             random.randint(-self.canvas_width + self.ball_rad, self.canvas_width - self.ball_rad),
                             random.randint(-self.canvas_height + self.ball_rad, self.canvas_height - self.ball_rad),
                             speed * _random_no_0(), speed * _random_no_0(),
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
        self.switch = 0
        self.start_time = time.time()
        self.speed_up_after = score_diff

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
        self.ui.goto(180, 240)
        self.ui.write(f"Score: {self.__score}", font=("Comic Sans MS", 30, "normal"))
        self.ui.goto(180, 310)
        self.ui.write(f"High Score: {max(self.__score_lst)}", font=("Comic Sans MS", 20, "normal"))
        self.ui.goto(-350, 240)
        self.ui.color("DarkRed")
        self.ui.write(f"LIFE: {self.player.life}", font=("Comic Sans MS", 30, "normal"))

    def check_dot_hit(self):
        for d in self.dots_lst:
            if self.player.distance(d) <= (d.radius + 10):
                self.__score += 1
                self.dots_lst.remove(d)

    def generate_dots(self):
        if len(self.dots_lst) <= self.num_dots - 2:
            d = dot.Dot(random.randint(-self.canvas_width + 20, self.canvas_width - 20),
                        random.randint(-self.canvas_height + 20, self.canvas_height - 20))
            self.dots_lst.append(d)

    def speed_up(self, ball):
        if self.__score >= self.speed_up_after:
            ball.vx += (self.__score - self.speed_up_after) * 0.001 / 5
            ball.vy += (self.__score - self.speed_up_after) * 0.001 / 5

    def __run(self):
        self.player.life = 3
        self.player.be_immune()  # let player be immune at the start
        self.player.body.showturtle()
        self.__draw_border()
        turtle.hideturtle()
        for ball in self.ball_list:
            ball.draw()

        self.player.controlled()
        self.player.screen.listen()

        while True:
            # PLAYER
            self.player.check_wall()
            self.player.body.showturtle()
            self.player.movement()
            self.player.undash()
            # DOTS
            self.check_dot_hit()
            self.generate_dots()

            # ball collision
            for ball in self.ball_list:
                ball.move(self.dt)
                # speed up as you go high
                self.speed_up(ball)
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
            turtle.clear()
            self.ui.clear()
            self.in_game_ui()
            self.__redraw()
            if self.player.life == 0:
                break
            self.player.stop_immune()

        self.__score_lst.append(self.__score)
        self.game_over()

    def set_start(self):
        self.start = True  #for turtle to use

    def title_ui(self):
        turtle.hideturtle()
        self.ui.color("black")
        self.ui.goto(0, 50)
        self.ui.write("DOT DASH DODGE", font=("Courier", 50, "bold"), align="center")

    def switch_color(self):
        if time.time() - self.start_time >= 0.5:
            self.start_time = time.time()
            if self.switch == 0:
                self.switch = 1
            else:
                self.switch = 0

    def press_space(self, color_lst: list, y, size=20):
        self.switch_color()
        self.ui.color(color_lst[self.switch])
        self.ui.goto(0, y)
        self.ui.write(f"press SPACE to restart", font=("Courier", size, "bold"), align="center")

        turtle.onkey(self.set_start, "space")  # press space to start

    def title(self):
        color_lst = ["green", "green3"]
        turtle.hideturtle()
        self.player.screen.listen()
        self.player.body.hideturtle()
        self.start_time = time.time()
        while True:
            # Changing color off ui so cool aa ><
            self.switch_color()
            turtle.clear()
            self.ui.clear()
            self.title_ui()
            self.press_space(color_lst, 0, 30)
            turtle.update()  # don't dare u remove this line this is life
            if self.start:
                break
        self.ui.clear()
        self.start = False
        self.__tutorial()

    def __tutorial(self):
        self.player.reset_movement()
        turtle.hideturtle()
        colorlst = ["green", "green3"]
        self.start_time = time.time()
        while True:
            # title
            turtle.clear()
            self.ui.clear()
            self.__draw_border()
            self.ui.color("black")
            self.ui.goto(0, 200)
            self.ui.write("HOW TO PLAY", font=("Courier", 50, "bold"), align="center")

            # Introduce Player
            self.ui.goto(-220, 150)
            self.ui.write("This is you, Use WASD to control.", font=("Courier", 20, "normal"), align="left")
            turtle.penup()
            turtle.pensize(3)
            turtle.color("blue")
            turtle.goto(-280, 160)
            turtle.setheading(0)
            turtle.pendown()
            turtle.begin_fill()
            for _ in range(3):
                turtle.forward(30)
                turtle.left(120)
            turtle.end_fill()

            # Introduce Immunizing system
            self.ui.goto(-220, 70)
            self.ui.write("After Hitting a ball, \nYou will be immune for a while(2s).",
                          font=("Courier", 20, "normal"), align="left")
            turtle.penup()
            turtle.pensize(3)
            turtle.color("gray")
            turtle.goto(-280, 90)
            turtle.setheading(0)
            turtle.pendown()
            turtle.begin_fill()
            for _ in range(3):
                turtle.forward(30)
                turtle.left(120)
            turtle.end_fill()

            # Introducing Balls
            self.ui.goto(-200, 5)
            self.ui.write("Dodge This",
                          font=("Courier", 20, "normal"), align="left")
            turtle.penup()
            turtle.pensize(3)
            turtle.color("red")
            turtle.goto(-250, 0)
            turtle.setheading(0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(30)
            turtle.end_fill()

            # Introducing dots
            self.ui.goto(-200, -70)
            self.ui.write("Get these green dots, for scores.",
                          font=("Courier", 20, "normal"), align="left")
            turtle.penup()
            turtle.pensize(3)
            turtle.color("green")
            turtle.goto(-250, -50)
            turtle.setheading(0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(1)
            turtle.end_fill()

            self.ui.goto(-200, -120)
            self.ui.write("press SPACEBAR to dash",
                          font=("Courier", 20, "normal"), align="left")

            self.ui.goto(-200, -170)
            self.ui.write("You Have 3 Life, GOODLUCK.",
                          font=("Courier", 20, "bold"), align="left")

            self.press_space(colorlst, -230, 30)

            turtle.update()  # don't dare u remove this line. this is life

            if self.start:
                break
        self.ui.clear()
        self.__run()

    def game_over(self):
        self.start = False
        score = self.__score
        highest = max(self.__score_lst)
        color_lst = ["DeepPink4", "DeepPink3"]
        self.start_time = time.time()
        self.__score = 0
        while True:
            self.ui.color("black")
            self.ui.goto(0, 80)
            self.ui.write("GAME OVER", font=("Courier", 50, "bold"), align="center")

            self.ui.color("DarkRed")
            self.ui.goto(0, 10)
            self.ui.write(f"Score: {score}", font=("Courier", 30, "bold"), align="center")

            self.ui.goto(0, -20)
            self.ui.write(f"High Score: {highest}", font=("Courier", 20, "bold"), align="center")
            self.press_space(color_lst, -100)
            if self.start:
                break

            turtle.update()  # don't delete this. this is life
        self.resetting()
        self.__run()

    def resetting(self):
        self.player.body.hideturtle()  # hiding the body. hehehe
        turtle.clear()
        self.ui.clear()
        del self.player
        self.__init__(self.num_balls, self.num_dots, self.size, self.speed, self.player_speed, self.speed_up_after,
                      score_lst=self.__score_lst)
