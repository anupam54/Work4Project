# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:23:59 2020

@author: Anupam kumar
"""


import cv2
from matplotlib import pyplot as plt

grey_img = cv2.imread("RGB to various color space/Images/nemo0.jpg",0)
color_img = cv2.imread("RGB to various color space/Images/nemo0.jpg",1)

print(grey_img)
print(color_img)

cv2.imshow("Grey Image", grey_img)
cv2.imshow("Color Image", color_img)

cv2.waitKey(0)
cv2.destroyAllWindows()