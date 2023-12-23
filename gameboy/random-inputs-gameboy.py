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
allKeys = ['UP','DOWN','LEFT','RIGHT','A','B','SELECT','START']

# pick random number
def randomNumber():
    numOfKeys = len(allKeys)-1
    # randomly choose number
    return random.randint(0,numOfKeys)

def executeAction(key, action):
    pressTime = random.uniform(0.1,1.0)
    holdTime = random.uniform(3.0,5.0)
    match action:
        case 'press':
            HoldAndReleaseKey(key,pressTime)
        case 'hold':
            HoldAndReleaseKey(key,holdTime)
    

# execute key press
def pressKey(number):
    key = allKeys[number]
    actions = ['press','hold']
    action = actions[random.randint(0,1)]
    match key:
        case 'L':
            executeAction(Q, 'press')
        case 'R':
            executeAction(E, 'press')
        case 'UP':
            executeAction(W, action)
        case 'DOWN':
            executeAction(S, action)
        case 'LEFT':
            executeAction(A, action)
        case 'RIGHT':
            executeAction(D, action)
        case 'A':
            executeAction(C, 'press')
        case 'B':
            executeAction(X, 'press')
        case 'SELECT':
            selectChance = random.randint(0,10)
            if selectChance == 0:
                executeAction(Z, 'press')
        case 'START':
            startChance = random.randint(0,10)
            if startChance == 0:
                executeAction(V, 'press')

# script loop
sleepTime = 0.1
print("Script is running!")
while True:
    pressKey(randomNumber())
    sleep(sleepTime)


