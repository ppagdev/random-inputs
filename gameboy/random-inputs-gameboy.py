import random
from time import sleep
from keycodes import *

# all buttons:
# L       = 'q'
# R       = 'e'
# UP      = 'w'
# DOWN    = 's'
# LEFT    = 'a'
# RIGHT   = 'd'
# A       = 'c'
# B       = 'x'
# SELECT  = 'z'
# START   = 'v'

# pick random number
def randomNumber():
    totalKeys = 10
    # randomly choose number between 0 and totalKeys
    return random.randint(0,totalKeys)

# execute key press
def pressKey(number):
    match number:
        case 0:
            HoldAndReleaseKey(Q,1)
        case 1:
            HoldAndReleaseKey(E,1)
        case 2:
            HoldAndReleaseKey(W,1)
        case 3:
            HoldAndReleaseKey(S,1)
        case 4:
            HoldAndReleaseKey(A,1)
        case 5:
            HoldAndReleaseKey(D,1)
        case 6:
            HoldAndReleaseKey(C,1)
        case 7:
            HoldAndReleaseKey(X,1)
        case 8:
            HoldAndReleaseKey(Z,1)
        case 7:
            HoldAndReleaseKey(V,1)

# script loop
sleepTime = 0.2
print("Script is running!")
while True:
    pressKey(randomNumber())
    sleep(sleepTime)


