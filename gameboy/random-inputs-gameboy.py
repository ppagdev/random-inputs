from multiprocessing import Process, freeze_support, set_start_method
import random
from time import sleep
from keycodes import *

# all buttons:
#################################
DPAD_UP      = W
DPAD_DOWN    = S
DPAD_LEFT    = A
DPAD_RIGHT   = D
#################################
CONSOLE_L       = Q
CONSOLE_R       = E
CONSOLE_SELECT  = Z
CONSOLE_START   = V
#################################
CONSOLE_A       = C
CONSOLE_B       = X
#################################

myActions = []

def addAction(action,frequency):
    for i in range(frequency):
        myActions.append(action)

#################################
addAction(DPAD_UP, 1)
addAction(DPAD_DOWN, 1)
addAction(DPAD_LEFT, 1)
addAction(DPAD_RIGHT, 1)
#################################
addAction(CONSOLE_L, 0)
addAction(CONSOLE_R, 0)
addAction(CONSOLE_SELECT, 1)
addAction(CONSOLE_START, 1)
#################################
addAction(CONSOLE_A, 1)
addAction(CONSOLE_B, 1)
#################################

currentList = myActions

#OVERRIDES
def overrides(action):
    if action == CONSOLE_START:
        if random.randint(0,10) == 0:
            return action
        else:
            return 'cancel'
    if action == CONSOLE_SELECT:
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
            continue
        print('P' + str(processIndex) + ': ' + str(action))
        pressTime = random.uniform(0.1,2.5)
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
    for i in range(2):
        Process(target=processAction, args=(i+1,)).start()
