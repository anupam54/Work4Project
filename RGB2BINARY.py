# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:44:07 2020

@author: Anupam kumar
"""


import cv2
import glob

path = "Images/*"

for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    print(a)
    
    c = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
    # cv2.imshow("Color Image",c)
    
    (thresh, nemo_bw) = cv2.threshold(c, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("Color Image",nemo_bw)
    
    cv2.waitKey()
    cv2.destroyAllWindows()