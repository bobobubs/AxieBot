# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 01:41:06 2021
@author: macwr
"""
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time
from CardSelector import cardDetection
import random
import mouse

CARD_TOP_LEFT_X = 186
CARD_TOP__LEFT_Y = 1150
CARD_BOTTOM_RIGHT_X = 2412
CARD_BOTTOM_RIGHT_Y = 1300

def endTurn():
    #select random coordinates withing the "End Turn" box
    x = random.randint(2233, 2499)
    y = random.randint(976, 1055)
    
    #move to and click on the box
    mouse.move(x, y, absolute = True, duration = 0.2)
    mouse.click('left')

def pickCard():
    x = random.randint(CARD_TOP_LEFT_X, CARD_BOTTOM_RIGHT_X)
    y = random.randint(CARD_TOP__LEFT_Y, CARD_BOTTOM_RIGHT_Y)
    
    moveTime = random.randint(10, 50)
    moveTime =  moveTime / 100
    
    #move to and click on the box
    mouse.move(x, y, absolute = True, duration = moveTime)
    mouse.click('left')


def main():
    count = 0
    numCards = random.randint(5, 7)
    while True:
        if count < numCards:
            pickCard()
            count += 1
            sleepTime = random.randint(10, 100)
            sleepTime =  sleepTime / 100
            time.sleep(sleepTime)
        else:
            endTurn()
            sleepTime = random.randint(20, 30)
            sleepTime =  sleepTime / 1.01
            time.sleep(sleepTime)
            numCards = random.randint(5, 7)
            count = 0


if __name__ == "__main__":
    main()