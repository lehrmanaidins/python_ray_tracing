"""
    Image Class
    @author Lehrman, Aidin
"""

import numpy as np
import matplotlib.pyplot as plt
from Color import *
from Vector3 import *

# Image
IMAGE_HEIGHT: int = 256 # Height of image
IMAGE_WIDTH: int = 256 # Width of image

# Creates 2D array of [r, g, b] colors with width 'image_width' and height 'image_height'
image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 3))

for j in range(IMAGE_HEIGHT): # For each row
    
    scanlines_remaining = IMAGE_HEIGHT - j # Calculates the amount of rows remaining
    
    # Prints progress bar and percent
    print(f"\rScanlines Remaining:\t{' ' * ( 3 - len(str(scanlines_remaining)))}{scanlines_remaining}\t|{'#' * math.floor(j / 20)}{' ' * math.floor(scanlines_remaining / 20)}|\t{j / IMAGE_HEIGHT * 100:.2f}%", end='')
    
    for i in range(IMAGE_WIDTH): # For each pixel in each row
        
        pixel_color = Color(i / (IMAGE_WIDTH - 1), j / (IMAGE_HEIGHT - 1), 0) # Gets pixel colors based on pixel's (x, y) values
        image[i, j] = np.clip(pixel_color.to_list(), 0, 1) # Sets pixel color to 'pixel_color'

plt.imsave('image.png', image) # Saves image
