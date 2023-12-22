import random

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

# button to start/stop script execution
def toggleScript():
    return
    # toggle script logic

# pick random number
def randomNumber():
    totalKeys = 10
    # randomly choose number between 0 and totalKeys
    return random.randint(0,totalKeys)
print(randomNumber())
# execute key press
# def pressKey(num):
#     switch (num)
#     {
#         case 0: key.press(some key),
#         # etc
#     }
