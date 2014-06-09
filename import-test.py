import numpy as np
import scipy
import scipy.misc
import scipy.ndimage
import matplotlib as mpl
import matplotlib.pyplot as plt
import Image

x = scipy.ndimage.imread('template-6.png')
x_remap = np.memmap('template-6.png', dtype=np.int64, shape=(50, 50))
lena = scipy.misc.lena()

plt.imshow(lena)

print type(x)
print x.shape, x.dtype
print type(x_remap)
#print type(lena)
#print lena.mean()
#print lena
