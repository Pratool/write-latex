"""
Detect corner points using the Harris corner detector and determine
subpixel position of corners.
"""

from matplotlib import pyplot as plt

from skimage import data
from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.transform import warp, AffineTransform
from skimage.draw import ellipse


tform = AffineTransform(scale=(1.3, 1.1), rotation=1, shear=0.7, translation=(210, 50))
image = warp(data.checkerboard(), tform.inverse, output_shape=(350, 350))

plt.imshow(image, cmap='gray', interpolation='nearest')
plt.show()
