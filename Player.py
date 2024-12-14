import time
import turtle
import math


class Player:
    def __init__(self, width: float, height: float, speed: float =0.8):
        self.move = True
        self.body = turtle.Turtle()
        self.body.shape('triangle')
        self.body.color('blue')
        self.body.penup()
        self.body.speed(1)
        self.status = True
        self.life = 3
        self.__default_speed = speed
        self.speed = self.__default_speed
        self.body.speed(self.speed)
        self.body.setheading(90)
        self.keys = {"w": False, "s": False, "a": False, "d": False,
                     "upwall": False, "leftwall": False, "rightwall": False, "downwall": False}
        self.screen = turtle.Screen()
        self.canvas_width = width
        self.canvas_height = height
        self.dashtime = 0
        self.immunity = False
        self.immunetime = 0

    def movement(self):
        if self.keys["w"] and (not self.keys["upwall"]) and self.move:
            self.body.goto(self.body.xcor(), self.body.ycor() + self.speed)
        if self.keys["s"] and (not self.keys["downwall"]):
            self.body.goto(self.body.xcor(), self.body.ycor() - self.speed)
        if self.keys["a"] and (not self.keys["leftwall"]):
            self.body.goto(self.body.xcor() - self.speed, self.body.ycor())
        if self.keys["d"] and (not self.keys["rightwall"]):
            self.body.goto(self.body.xcor() + self.speed, self.body.ycor())
        turtle.update()

    def c_keys(self, key, value):
        self.keys[key] = value

    def check_wall(self):
        if self.move:
            if self.body.xcor() >= self.canvas_width - 15:
                self.keys["rightwall"] = True
            else:
                self.keys["rightwall"] = False

            if self.body.xcor() <= -self.canvas_width + 15:
                self.keys["leftwall"] = True
            else:
                self.keys["leftwall"] = False

            if self.body.ycor() >= self.canvas_height - 17:
                self.keys["upwall"] = True
            else:
                self.keys["upwall"] = False

            if self.body.ycor() <= -self.canvas_height + 13:
                self.keys["downwall"] = True
            else:
                self.keys["downwall"] = False

    def dash(self, status):
        self.speed = self.__default_speed + (status * 2)
        self.dashtime = time.time()

    def undash(self):
        rn = time.time()
        if self.dashtime != 0 and rn >= self.dashtime + 0.25:
            self.dashtime = 0
            self.speed = self.__default_speed

    def controlled(self):
        self.screen.onkeypress(lambda: self.c_keys("w", True), "w")
        self.screen.onkeyrelease(lambda: self.c_keys("w", False), "w")
        self.screen.onkeypress(lambda: self.c_keys("s", True), "s")
        self.screen.onkeyrelease(lambda: self.c_keys("s", False), "s")
        self.screen.onkeypress(lambda: self.c_keys("a", True), "a")
        self.screen.onkeyrelease(lambda: self.c_keys("a", False), "a")
        self.screen.onkeypress(lambda: self.c_keys("d", True), "d")
        self.screen.onkeyrelease(lambda: self.c_keys("d", False), "d")
        self.screen.onkeypress(lambda: self.dash(True), "space")

    def distance(self, that):
        return math.sqrt((self.body.xcor() - that.x) ** 2 + (self.body.ycor() - that.y) ** 2)

    def be_immune(self):
        self.immunity = True
        self.immunetime = time.time()
        self.body.color('gray')

    def stop_immune(self):
        rn = time.time()
        if self.immunetime != 0 and rn >= self.immunetime + 2:
            self.immunity = False
            self.body.color('blue')

    def disable_movement(self):
        k = list(self.keys.keys())[4:8]
        for key in k:
            self.keys[key] = True
        self.move = False

    def reset_movement(self):
        k = list(self.keys.keys())
        for key in k:
            self.keys[key] = False
        self.move = True
