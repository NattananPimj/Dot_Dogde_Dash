import turtle


class Player:
    def __init__(self):
        self.body = turtle.Turtle()
        self.body.shape('triangle')
        self.body.color('blue')
        self.body.penup()
        self.body.speed(1)
        self.status = True
        self.life = 3
        self.position = (0, 0)
        self.speed = 2
        self.body.speed(self.speed)
        self.body.setheading(90)
        self.keys = {"w": False, "s": False, "a": False, "d": False}

    def movement(self):
        if self.keys["w"]:
            self.body.goto(self.body.xcor(), self.body.ycor() + self.speed)
        if self.keys["s"]:
            self.body.goto(self.body.xcor(), self.body.ycor() - self.speed)
        if self.keys["a"]:
            self.body.goto(self.body.xcor() - self.speed, self.body.ycor())
        if self.keys["d"]:
            self.body.goto(self.body.xcor() + self.speed, self.body.ycor())
        turtle.update()

    def c_keys(self, key, value):
        self.keys[key] = value

    def dash(self, status):
        self.speed = 2 + (status * 10)


player = Player()
wn = turtle.Screen()
wn.onkeypress(lambda: player.c_keys("w", True), "w")
wn.onkeyrelease(lambda: player.c_keys("w", False), "w")
wn.onkeypress(lambda: player.c_keys("s", True), "s")
wn.onkeyrelease(lambda: player.c_keys("s", False), "s")
wn.onkeypress(lambda: player.c_keys("a", True), "a")
wn.onkeyrelease(lambda: player.c_keys("a", False), "a")
wn.onkeypress(lambda: player.c_keys("d", True), "d")
wn.onkeyrelease(lambda: player.c_keys("d", False), "d")
# hope user don't hold space plssss just don't I don't know how to make them properly this shit is just a witchcraft
# this shouldn't be for speeding
wn.onkeypress(lambda: player.dash(True), "space")
wn.onkeyrelease(lambda: player.dash(False), "space")

wn.listen()

while True:
    player.movement()
