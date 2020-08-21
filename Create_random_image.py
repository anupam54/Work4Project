# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:08:29 2020

@author: Anupam kumar
"""


import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_int

random_image = np.random.random([500,500])
# plt.imshow(random_image)
print(random_image)
print(random_image.min(), random_image.max())

my_int_img = img_as_int(random_image)
print(my_int_img.min(), my_int_img.max())

plt.imshow(my_int_img)
