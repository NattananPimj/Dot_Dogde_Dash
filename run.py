import Game
import turtle

# fixable variable
'''
The game may run differently depends on computer, if you felt the balls of player move to fast or slow than it should,
you can adjust them at BALL_SPEED and PLAYER_SPEED, respectively

If you want more difficulty, set this up

Medium MODE:
NUM_DOTS = 10
NUM_BALL = 10
SIZE = 0.05

Hard MODE:
NUM_DOTS = 10
NUM_BALL = 15 or more
SIZE = 0.05
BALL_SPEED = 20

'''
NUM_BALL = 5  # default 5
NUM_DOTS = 15  # default = 15
SIZE = 0.1  # default = 0.1
BALL_SPEED = 10  # default = 10
PLAYER_SPEED = 0.8  # default = 0.8


run = Game.RunGame(NUM_BALL, NUM_DOTS, SIZE, BALL_SPEED, PLAYER_SPEED)
run.title()
turtle.done()
