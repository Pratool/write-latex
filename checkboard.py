"""
This draws a checkerboard onto the screen and saves it as a PNG file.
implementation note: you can use scipy to interpolate a matrix with nearest neighbor
"""

import numpy as np
from PIL import Image
from scipy.ndimage.interpolation import zoom

import matplotlib
import matplotlib.pyplot as plt

import skimage
from skimage import data, filter, io, color
from skimage.transform import rescale
from skimage.transform import resize

check = np.zeros((9, 9))
check[::2, 1::2] = 1
check[1::2, ::2] = 1

plt.imshow(check, cmap='gray', interpolation='nearest')
plt.show()

io.imsave('check.png', check)
