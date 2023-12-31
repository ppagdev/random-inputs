import random
from time import sleep
from keycodes import *

# all buttons:
#################################
CPAD_LEFT     =   NUMPAD_4
CPAD_RIGHT    =   NUMPAD_6
CPAD_UP       =   NUMPAD_8
CPAD_DOWN     =   NUMPAD_5
#################################
DPAD_LEFT     =   F
DPAD_RIGHT    =   H
DPAD_UP       =   T
DPAD_DOWN     =   G
#################################
CSTICK_LEFT      =   J
CSTICK_RIGHT     =   L
CSTICK_UP        =   I
CSTICK_DOWN      =   K
#################################
CONSOLE_A = A
CONSOLE_B = S
CONSOLE_X = Z
CONSOLE_Y = X
#################################
CONSOLE_L     = Q
CONSOLE_R     = W
CONSOLE_ZL    = NUMPAD_1
CONSOLE_ZR    = NUMPAD_2
#################################
CONSOLE_START   = M
CONSOLE_SELECT  = N
CONSOLE_HOME    = B
CONSOLE_POWER   = V
#################################



#####################################
# Pokemon XY
#####################################
# RUN_LEFT     =   DPAD_LEFT    +   B
# RUN_RIGHT    =   DPAD_RIGHT   +   B
# RUN_UP       =   DPAD_UP      +   B
# RUN_DOWN     =   DPAD_DOWN    +   B



allActions = [CPAD_LEFT, CPAD_RIGHT, CPAD_UP, CPAD_DOWN, DPAD_LEFT, DPAD_RIGHT, DPAD_UP, DPAD_DOWN, CSTICK_LEFT, CSTICK_RIGHT, CSTICK_UP, CSTICK_DOWN, CONSOLE_A, CONSOLE_B, CONSOLE_Y, CONSOLE_X, CONSOLE_L, CONSOLE_R, CONSOLE_ZL, CONSOLE_ZR, CONSOLE_START, CONSOLE_SELECT, CONSOLE_HOME, CONSOLE_POWER, 'RUN_DOWN', 'RUN_LEFT', 'RUN_RIGHT', 'RUN_UP']

# pick random action
def randomAction():
    numOfActions = len(allActions)-1
    # randomly choose action
    return allActions[random.randint(0,numOfActions)]

# process action
def processAction(action):
    pressTime = random.uniform(0.1,1.0)
    match action:
        case 'RUN_DOWN':
            HoldKey(CONSOLE_B)
            HoldAndReleaseKey(DPAD_DOWN, pressTime)
            ReleaseKey(CONSOLE_B)
        case 'RUN_UP':
            HoldKey(CONSOLE_B)
            HoldAndReleaseKey(DPAD_UP, pressTime)
            ReleaseKey(CONSOLE_B)
        case 'RUN_LEFT':
            HoldKey(CONSOLE_B)
            HoldAndReleaseKey(DPAD_LEFT, pressTime)
            ReleaseKey(CONSOLE_B)
        case 'RUN_RIGHT':
            HoldKey(CONSOLE_B)
            HoldAndReleaseKey(DPAD_RIGHT, pressTime)
            ReleaseKey(CONSOLE_B)
        case default:
            HoldAndReleaseKey(action,pressTime)

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
    processAction(randomAction())
    sleep(sleepTime)


