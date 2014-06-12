import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

lena = mpimg.imread('lena.png')

print lena.mean()

plt.imshow(lena[200:220, 200:220], cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.show()
