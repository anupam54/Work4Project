# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:19:51 2020

@author: Anupam kumar
"""


#Matplotlib
# pyplot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img = mpimg.imread("Images/nemo0.jpg")
# print(type(img))
# print(img.shape)
plt.imshow(img)
plt.colorbar("Images/nemo0.jpg")
