from multiprocessing import Process, freeze_support, set_start_method
import random
from time import sleep
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys

showKeys()

# all buttons:
#################################
FORWARD         = 'W'
#################################

myActions = []

def addAction(action,frequency):
    for i in range(frequency):
        myActions.append(action)

#################################
addAction(FORWARD, 1)
#################################

currentList = myActions

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
        print('P' + str(processIndex) + ': ' + str(action))
        press(action,pressTime)

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
