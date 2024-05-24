import os
import signal
import sys
from multiprocessing import Process, freeze_support, set_start_method
import random
from time import sleep
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import subprocess

myActions = dict(
# all buttons:
#################################
forward = 'q',
back = 'w',
left = 'e',
right = 'r',
################################
move_camera = 'MOVE_MOUSE',
################################
left_hand = 't',
right_hand = 'y',
activate = 'u',
sheathe = 'i',
jump = 'o',
sprint = 'p',
power = 'a',
sneak = 's',
menu = 'MENU',
)

currentList = list(myActions.keys())

# pick random action
def randomAction():
    numOfActions = len(currentList)-1
    # randomly choose action
    return currentList[random.randint(0,numOfActions)]

# process action
def processAction(processIndex):
    try:
        while True:
            pressTime = random.uniform(0.1, 10.0)
            action_name = randomAction()
            action = myActions[action_name]
            print('P' + str(processIndex) + ': ' + str(action_name) + ', ' + str(round(pressTime, 2)) + ' seconds')

            if action == 'MOVE_MOUSE':
                subprocess.call(["xdotool", "mousemove_relative", str(random.randint(-200, 200)), str(random.randint(-200, 200))])
                continue
            elif action == 'MENU':
                action = random.choice(['d','f','g'])

            elif action == 'LEFT_CLICK':
                subprocess.call(["xdotool", "click", "1"])
                continue
            elif action == 'RIGHT_CLICK':
                subprocess.call(["xdotool", "click", "3"])
                continue

            press(action, pressTime)
    except KeyboardInterrupt:
        os.kill(os.getpid(), signal.SIGINT)

#countdown
def countdown():
    print("Starting in ")
    sleep(0.5)
    for i in range(3,0,-1):
        print(i)
        sleep(1)
    print("Script is running!")

if __name__ == '__main__':
    try:
        countdown()
        freeze_support()
        set_start_method('spawn')
        for i in range(5):
            Process(target=processAction, args=(i+1,)).start()
    except KeyboardInterrupt:
        print("Releasing all keys...")
        for key in currentList:
            try:
                releaseKey(key)
            except:
                continue
        print("Done! Exiting program...")
        sys.exit()
