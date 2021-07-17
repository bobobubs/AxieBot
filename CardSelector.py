# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 11:27:19 2021

@author: macwr
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2


def cardDetection(image):
    # read the image
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayscale, 30, 100)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    
    
    
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (20, 220, 20), 3)
    
    #print(lines[0][0])
    plt.imshow(image)
    plt.show()
    return lines

image = cv2.imread("pickingCards.png")
cardDetection(image)