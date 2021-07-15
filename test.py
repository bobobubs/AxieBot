# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:08:54 2021

@author: macwr
"""

import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab


top, bottom, left, right = None, None, None, None
#initiate the screen to read data from it
cap =  ImageGrab.grab(bbox = (0,0,100,500))
    


while True:
    
    if top and bottom !=None:
        #print("window should be different")
        cap =  ImageGrab.grab(bbox = (top, left, bottom, right))
        cap_arr = np.array(cap)
        cv2.imshow("", cap_arr)    
        1
    else:
        #print("top or bottom is not set")
        cap =  ImageGrab.grab(bbox = (0,0,100,500))
        cap_arr = np.array(cap)
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
        print(top)
        print(left)
    
    #if you pressed 2
    #save the position of the bottom right corner of the screen
    if keypress == ord("2"):
        bottomRight = pyautogui.position()
        bottom = bottomRight.y
        right = bottomRight.x
        print(bottom)
        print(right)
    
    #if you pressed the spacebar
    #resize the window
    if keypress == 32: 
        print("spacebar")
        #check to see that the dimensions of the axie window have been set
        if top and bottom != None:
            print("top = ", top)
            cap = ImageGrab.grab(bbox=(top, left, bottom, right))
        
        else:
            continue
            
    
cv2.destroyAllWindows()