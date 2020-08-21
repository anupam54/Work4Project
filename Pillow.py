# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:34:21 2020

@author: Anupam kumar
"""


# pillow
from PIL import Image
import numpy as np
img = Image.open("Images/nemo0.jpg") 
print(type(img))

# img.show()
print(img.format)

img1 = np.asarray(img)
print(img1)