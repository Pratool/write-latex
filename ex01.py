"""
Exercise 1
Opens scikit-image logo, crops and displays it, then transforms and saves
the image as PNG, JPG, and TIFF.
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import matplotlib

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989*r + 0.5870*g + 0.1140*b

    return gray

logo = mpimg.imread('scikit-image.png')
logo = logo[1:103, 1:103]
logo = rgb2gray(logo)

imgplot = plt.imshow(logo, cmap=plt.cm.gray, interpolation='nearest')
plt.show()
