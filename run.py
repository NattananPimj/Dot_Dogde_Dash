import Game
import turtle

# fixable variable
'''
DOT DODGE DASH (Modifier) : if does not want to modify anything, just run.


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

DEV NOTE: If you want to add more ball, I suggest to increase the player speed

DISCLAIMER: IT WORK ON MY COMPUTER AND TWO OF MY FRIENDS' one pycharm, one vs code.
'''
NUM_BALL = 5  # Number of red balls: default 5
NUM_DOTS = 15  # Number of dots: default = 15
SIZE = 0.1  # Size of red ball: default = 0.1
BALL_SPEED = 10  # Speed of Red balls: default = 10
PLAYER_SPEED = 0.8  # Speed of player: default = 0.8
BALL_SPEEDING_AFTER = 40  # The score that balls will start speeding: default = 40


run = Game.RunGame(NUM_BALL, NUM_DOTS, SIZE, BALL_SPEED, PLAYER_SPEED, BALL_SPEEDING_AFTER)
run.title()
turtle.done()
