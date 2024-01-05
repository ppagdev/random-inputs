from multiprocessing import Process, freeze_support, set_start_method
import random
from time import sleep
from keycodes import *

# all buttons:
#################################
CPAD_LEFT     =   LEFT_BRACKET
CPAD_RIGHT    =   RIGHT_BRACKET
CPAD_UP       =   APOSTROPHE
CPAD_DOWN     =   BACKSLASH
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

myActions = []

def addAction(action,frequency):
    for i in range(frequency):
        myActions.append(action)

#################################
addAction(CPAD_LEFT, 1)
addAction(CPAD_RIGHT, 1)
addAction(CPAD_UP, 1)
addAction(CPAD_DOWN, 1)
#################################
addAction(DPAD_LEFT, 1)
addAction(DPAD_RIGHT, 1)
addAction(DPAD_UP, 1)
addAction(DPAD_DOWN, 1)
#################################
addAction(CSTICK_LEFT, 1)
addAction(CSTICK_RIGHT, 1)
addAction(CSTICK_UP, 1)
addAction(CSTICK_DOWN, 1)
#################################
addAction(CONSOLE_A, 1)
addAction(CONSOLE_B, 1)
addAction(CONSOLE_X, 1)
addAction(CONSOLE_Y, 1)
#################################
addAction(CONSOLE_L, 1)
addAction(CONSOLE_R, 1)
addAction(CONSOLE_ZL, 0)
addAction(CONSOLE_ZR, 0)
#################################
addAction(CONSOLE_START, 1)
addAction(CONSOLE_SELECT, 0)
addAction(CONSOLE_HOME, 0)
addAction(CONSOLE_POWER, 0)
#################################

currentList = myActions

#OVERRIDES
def overrides(action):
    if action == CONSOLE_START:
        if random.randint(0,10) == 0:
            return action
        else:
            return 'cancel'
    if action ==  CONSOLE_X:
        if random.randint(0,10) == 0:
            return action
        else:
            return 'cancel'
    else:
        return action

# pick random action
def randomAction():
    numOfActions = len(currentList)-1
    # randomly choose action
    return currentList[random.randint(0,numOfActions)]

# process action
def processAction(processIndex):
    while True:
        action = randomAction()
        if overrides(action) == 'cancel':
            print('skip')
            continue
        print('P' + str(processIndex) + ': ' + str(action))
        pressTime = random.uniform(0.01,5.0)
        HoldAndReleaseKey(action,pressTime)

#countdown
def countdown():
    print("Starting in ")
    sleep(0.5)
    for i in range(3,0,-1):
        print(i)
        sleep(1)
    print("Script is running!")

if __name__ == '__main__':
    countdown()
    freeze_support()
    set_start_method('spawn')
    for i in range(3):
        Process(target=processAction, args=(i+1,)).start()
