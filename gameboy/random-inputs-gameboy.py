import random
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

# all buttons:
# L
# R
# UP
# DOWN
# LEFT
# RIGHT
# A
# B
# SELECT
# START

# pick random number
def randomNumber():
    totalKeys = 10
    # randomly choose number between 0 and totalKeys
    return random.randint(0,totalKeys)

# execute key press
# def pressKey(num):
#     switch (num)
#     {
#         case 0: key.press(some key),
#         # etc
#     }

# script loop
sleepTime = 1
while True:
    print(randomNumber())
    keyboard.press('p')
    keyboard.release('p')
    sleep(sleepTime)


