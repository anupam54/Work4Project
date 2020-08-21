# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:33:54 2020

@author: Anupam kumar
"""


#pipinstall scikit-image
from skimage import io
import matplotlib.pyplot as plt

image = io.imread("Images/nemo0.jpg")
print(type(image))
plt.imshow(image)
