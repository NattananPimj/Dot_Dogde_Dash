import time
import turtle
import math


class Player:
    def __init__(self, width: float, height: float, speed: float = 0.8):
        self.move = True
        self.body = turtle.Turtle()
        self.body.shape('triangle')
        self.body.color('blue')
        self.body.penup()
        self.body.speed(1)
        self.__life = 3
        self.__default_speed = speed
        self.speed = self.__default_speed
        self.body.speed(self.speed)
        self.body.setheading(90)
        self.__keys = {"w": False, "s": False, "a": False, "d": False,
                     "upwall": False, "leftwall": False, "rightwall": False, "downwall": False}
        self.screen = turtle.Screen()
        self.canvas_width = width
        self.canvas_height = height
        self.dashtime = 0
        self.immunity = False
        self.immunetime = 0

    def decrease_life(self):
        self.__life -= 1

    def reset_life(self):
        self.__life = 3

    @property
    def life(self):
        return self.__life

    def movement(self):
        if self.__keys["w"] and (not self.__keys["upwall"]) and self.move:
            self.body.goto(self.body.xcor(), self.body.ycor() + self.speed)
        if self.__keys["s"] and (not self.__keys["downwall"]):
            self.body.goto(self.body.xcor(), self.body.ycor() - self.speed)
        if self.__keys["a"] and (not self.__keys["leftwall"]):
            self.body.goto(self.body.xcor() - self.speed, self.body.ycor())
        if self.__keys["d"] and (not self.__keys["rightwall"]):
            self.body.goto(self.body.xcor() + self.speed, self.body.ycor())
        turtle.update()

    def c_keys(self, key, value):
        self.__keys[key] = value

    def check_wall(self):
        if self.move:
            if self.body.xcor() >= self.canvas_width - 15:
                self.__keys["rightwall"] = True
            else:
                self.__keys["rightwall"] = False

            if self.body.xcor() <= -self.canvas_width + 15:
                self.__keys["leftwall"] = True
            else:
                self.__keys["leftwall"] = False

            if self.body.ycor() >= self.canvas_height - 17:
                self.__keys["upwall"] = True
            else:
                self.__keys["upwall"] = False

            if self.body.ycor() <= -self.canvas_height + 13:
                self.__keys["downwall"] = True
            else:
                self.__keys["downwall"] = False

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
        k = list(self.__keys.keys())[4:8]
        for key in k:
            self.__keys[key] = True
        self.move = False

    def reset_movement(self):
        k = list(self.__keys.keys())
        for key in k:
            self.__keys[key] = False
        self.move = True
