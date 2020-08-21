# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:08:29 2020

@author: Anupam kumar
"""

from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_int

my_image = io.imread("RGB to various color space/Images/nemo0.jpg")
my_image[10:200, 10:200, :] = [0,0,255]
io.imshow(my_image)