"""
This draws a checkerboard onto the screen and saves it as a PNG file.
"""

import numpy as np
from PIL import Image

import matplotlib
import matplotlib.pyplot as plt

import skimage
from skimage import data, filter, io, color
from skimage.transform import rescale

check = np.zeros((9, 9))
check[::2, 1::2] = 1
check[1::2, ::2] = 1

plt.imshow(check, cmap='gray', interpolation='nearest')
plt.show()

check = rescale(check, 20, mode='nearest')
io.imsave('check.png', check)
