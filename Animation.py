# Imports

import os
import sys
import colorama
from colorama import Style
from colorama import Fore
from time import sleep

# Misc

colorama.init(autoreset=True)

# Variables

leftSide = ""
rightSide = ""
termWidth = os.get_terminal_size().columns
sleepTime = 1/termWidth
possibleColors = [Fore.MAGENTA, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.RED]

for i in range(3):
    colorKey = 0

    for j in range(termWidth):
        if i % 3 == 0:
            colorKey += 1
        if colorKey > len(possibleColors)-1:
            colorKey = 0
        rightSide += "#"
        leftSide = ""
        leftSideSize = termWidth - len(rightSide)
        for i in range(leftSideSize):
            leftSide += "\\"
        print(f"{Style.DIM}{leftSide}{Style.NORMAL}{possibleColors[colorKey]}{rightSide}")
        sleep(sleepTime)
    
    for j in range(termWidth):
        if i % 3 == 0:
            colorKey += 1
        if colorKey > len(possibleColors)-1:
            colorKey = 0
        leftSide += "\\"
        rightSide = ""
        rightSideSize = termWidth - len(leftSide)
        for i in range(rightSideSize):
            rightSide += "#"
        print(f"{Style.DIM}{leftSide}{Style.NORMAL}{possibleColors[colorKey]}{rightSide}")
        sleep(sleepTime)

