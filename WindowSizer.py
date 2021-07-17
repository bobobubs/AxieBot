# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:08:54 2021

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


#Initialize position vairables
top, bottom, left, right = None, None, None, None
#initiate the screen to read data from it
cap =  ImageGrab.grab(bbox = (0,0,500,300))
    

def pickCard(lines):
    print("New Loop")
    print(lines)
    n = random.randint(0, len(lines))
    line = lines[n][0]
    
    return line

count = 0 

while True:
    
    #Check to see if the window has been resized
    if top and bottom !=None:
        cap =  ImageGrab.grab(bbox = (left, top, right, bottom))
        cap_arr = np.array(cap)
        lines = cardDetection(cap_arr)
        line = pickCard(lines)
        if count < 4:
            #click on a line
            lineX = line[0]
            lineY = line[1]
            mouse.move(left + lineX,top + lineY, absolute = True, duration = 0.1)
            mouse.click('left')
            count += 1
        else:
            count = 0 
            continue
        
        cv2.imshow("", cap_arr)    
    else:
        cap =  ImageGrab.grab(bbox = (0,0,500,300))
        cap_arr = np.array(cap)
        lines = cardDetection(cap_arr)
        cv2.imshow("", cap_arr)    
    
        
    
    keypress = cv2.waitKey(1)
    
    #If you pressed esc
    #close the program
    if keypress == 27:
        break
    
    #if you pressed 1
    #save the position of the top left corner of the screen
    if keypress == ord("1"):
        topLeft = pyautogui.position()
        top = topLeft.y
        left = topLeft.x
    
    #if you pressed 2
    #save the position of the bottom right corner of the screen
    if keypress == ord("2"):
        bottomRight = pyautogui.position()
        bottom = bottomRight.y
        right = bottomRight.x
        
    time.sleep(1)
    
cv2.destroyAllWindows()


    