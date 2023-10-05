"""
    Image Class
    @author Lehrman, Aidin
"""

import numpy as np
import matplotlib.pyplot as plt
from Color import *
from Vector3 import *

# Image
image_height = 256 # Height of image
image_width = 256 # Width of image
image = np.zeros((image_height, image_width, 3)) # Creates 2D array of [r, g, b] colors with width 'image_width' and height 'image_height'

for j in range(image_height): # For each row
    
    scanlines_remaining = image_height - j # Calculates the amount of rows remaining
    
    # Prints progress bar and percent
    print(f"\rScanlines Remaining:\t{' ' * ( 3 - len(str(scanlines_remaining)))}{scanlines_remaining}\t|{'#' * (j / 20)}{' ' * (scanlines_remaining / 20)}|\t{j / image_height * 100:.2f}%", end='')
    
    for i in range(image_width): # For each pixel in each row
        
        pixel_color = Color(i / (image_width - 1), j / (image_height - 1), 0) # Gets pixel colors based on pixel's (x, y) values
        image[i, j] = np.clip(pixel_color.to_list(), 0, 1) # Sets pixel color to 'pixel_color'

plt.imsave('image.png', image) # Saves image
