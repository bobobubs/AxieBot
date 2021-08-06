# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 00:55:00 2021

@author: macwr
"""

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import time


img  = Image.open("test.png")
text = tess.image_to_string(img)
#text = text[:-5]
time.sleep(1)

print(repr(text))

