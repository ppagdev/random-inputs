from multiprocessing import Process, freeze_support, set_start_method
import random
from time import sleep
from keycodes import *

pydirectinput.FAILSAFE = False

# all buttons:
#################################
FORWARD         = W
STRAFE_LEFT     = A
BACK            = S
STRAFE_RIGHT    = D
#################################
JUMP    = SPACE
SPRINT  = G
SHOUT   = Z
SNEAK   = C
#################################
LEFT_HAND        = 'LEFT_MOUSE'
RIGHT_HAND       = 'RIGHT_MOUSE'
ACTIVATE         = E
SHEATHE          = R
#################################
CHARACTER_MENU      = TAB
ACCEPT              = ENTER
MOVE_CAMERA         = 'MOVE_MOUSE'
POV_TOGGLE          = F
#################################

myActions = []

def addAction(action,frequency):
    for i in range(frequency):
        myActions.append(action)

#################################
addAction(FORWARD, 1)
addAction(STRAFE_LEFT, 1)
addAction(BACK, 1)
addAction(STRAFE_RIGHT, 1)
#################################
addAction(JUMP, 1)
addAction(SPRINT, 1)
addAction(SHOUT, 1)
addAction(SNEAK, 1)
#################################
addAction(LEFT_HAND, 1)
addAction(RIGHT_HAND, 1)
addAction(ACTIVATE, 1)
addAction(SHEATHE, 1)
#################################
addAction(CHARACTER_MENU, 1)
addAction(ACCEPT, 1)
addAction(MOVE_CAMERA, 1)
addAction(POV_TOGGLE, 1)
#################################

currentList = myActions

#OVERRIDES
def overrides(action, pressTime):
    if action == CHARACTER_MENU:
        if random.randint(0,20) != 0:
            return 'done'
    if action == POV_TOGGLE:
        if random.randint(0,15) != 0:
            return 'done'
    # Mouse
    if action == 'MOVE_MOUSE':
        MouseMove(random.randint(-500,500), random.randint(-500,500))
        return 'done'
    if action == 'LEFT_MOUSE':
        MouseClick("left", pressTime)
        return 'done'
    if action == 'RIGHT_MOUSE':
        MouseClick("right", pressTime)
        return 'done'
    return action

# pick random action
def randomAction():
    numOfActions = len(currentList)-1
    # randomly choose action
    return currentList[random.randint(0,numOfActions)]

# process action
def processAction(processIndex):
    while True:
        pressTime = random.uniform(0.1,5.0)
        action = randomAction()
        if overrides(action, pressTime) == 'done':
            continue
        print('P' + str(processIndex) + ': ' + str(action))
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
    for i in range(5):
        Process(target=processAction, args=(i+1,)).start()
