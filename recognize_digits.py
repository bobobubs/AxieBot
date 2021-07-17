# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 17:39:13 2021

@author: macwr
"""

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract as tes

results = tes.image_to_string(Image.open('pickingCards.png'))