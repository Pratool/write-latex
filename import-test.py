import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def detach_display():
    img = mpimg.imread('template-6.png')

    print img

#    imgplot = plt.imshow(img)
    plt.imshow(img)
    plt.show()

detach_display()
