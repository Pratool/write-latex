"""
Exercise 1
Opens scikit-image logo, crops and displays it, then transforms and saves
the image as PNG and TIFF.
"""

import matplotlib.pyplot as plt
import matplotlib

import skimage
from skimage import data, filter, io, color
from skimage.transform import rescale

import numpy as np
from PIL import Image

filename = 'scikit-image.png'
logo = io.imread(filename)
logo = logo[1:103, 1:103]
logo = color.rgb2gray(logo)

imgplot = plt.imshow(logo, cmap=plt.cm.gray, interpolation='nearest')
plt.show()

io.imsave('ex01-outfile.png', logo)
io.imsave('ex01-outfile.tiff', logo)
