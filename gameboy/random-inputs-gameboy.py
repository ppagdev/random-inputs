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
    match action:
        case 'press':
            HoldAndReleaseKey(key, pressTime)
        case 'hold':
            ReleaseKey(W)
            ReleaseKey(S)
            ReleaseKey(A)
            ReleaseKey(D)
            HoldKey(key)

# execute key press
def pressKey(number):
    key = allKeys[number]
    actions = ['press','hold']
    if random.randint(0,3) == 0:
        action = actions[1]
    else:
        action = actions[0]
    print(action + '\t' + key)
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


#countdown
print("Starting in ")
sleep(0.5)
for i in range(3,0,-1):
    print(i)
    sleep(1)
    
# script loop
sleepTime = 0.1
print("Script is running!")
while True:
    pressKey(randomNumber())
    sleep(sleepTime)


