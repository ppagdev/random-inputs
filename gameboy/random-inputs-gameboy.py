import random
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

# all buttons:
L       = 'q'
R       = 'e'
UP      = 'w'
DOWN    = 's'
LEFT    = 'a'
RIGHT   = 'd'
A       = 'c'
B       = 'x'
SELECT  = 'z'
START   = 'v'

# pick random number
def randomNumber():
    totalKeys = 10
    # randomly choose number between 0 and totalKeys
    return random.randint(0,totalKeys)

# execute key press
def pressKey(number):
    match number:
        case 0:
            keyboard.press(L)
            keyboard.release(L)
        case 1:
            keyboard.press(R)
            keyboard.release(R)
        case 2:
            keyboard.press(UP)
            keyboard.release(UP)
        case 3:
            keyboard.press(DOWN)
            keyboard.release(DOWN)
        case 4:
            keyboard.press(LEFT)
            keyboard.release(LEFT)
        case 5:
            keyboard.press(RIGHT)
            keyboard.release(RIGHT)
        case 6:
            keyboard.press(A)
            keyboard.release(A)
        case 7:
            keyboard.press(B)
            keyboard.release(B)
        case 8:
            keyboard.press(SELECT)
            keyboard.release(SELECT)
        case 7:
            keyboard.press(START)
            keyboard.release(START)

# script loop
sleepTime = 0.2
print("Script is running!")
while True:
    pressKey(randomNumber())
    sleep(sleepTime)


