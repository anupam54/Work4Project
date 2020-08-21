# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:48:04 2020

@author: Anupam kumar
"""
from skimage import io


my_image = io.imread("RGB to various color space/Images/nemo0.jpg")
print(my_image)
io.imshow(my_image)

print(my_image.min(), my_image.max())