# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:42:05 2020

@author: Anupam kumar
"""


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("RGB to various color space/Images/nemo0.jpg",1)
# For GREY image put 0 and for COLORED image put 1
plt.imshow(img)