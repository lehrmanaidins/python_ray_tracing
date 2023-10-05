"""
    Image Class
    @author Lehrman, Aidin
"""

import numpy as np
import matplotlib.pyplot as plt
from colors import red, green, blue
from Color import *
from Vector3 import *

# Image
IMAGE_HEIGHT: int = 256 # Height of image
IMAGE_WIDTH: int = 256 # Width of image

# Creates 2D array of [r, g, b] colors with width 'image_width' and height 'image_height'
image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 3))

for j in range(IMAGE_HEIGHT): # For each row
    # Calculates the amount of rows remaining
    scanlines_remaining = IMAGE_HEIGHT - j
    
    # Progress
    completed: int = j // 5
    upcomming: int = (IMAGE_HEIGHT // 5) - completed

    # Prints progress bar and percent
    print("\rScanlines Remaining: ", end='')
    print(blue(f"{' ' * ( 3 - len(str(scanlines_remaining)))}{scanlines_remaining} "), end='')
    print(green(f"|{'#' * completed}{' ' * upcomming}| "), end='')
    print(red(f"{j / IMAGE_HEIGHT * 100:.2f}%\t"), end='')
    
    for i in range(IMAGE_WIDTH): # For each pixel in each row
        # Gets pixel colors based on pixel's (x, y) values
        pixel_color = Color(i / (IMAGE_WIDTH - 1), j / (IMAGE_HEIGHT - 1), 0)
        # Sets pixel color to 'pixel_color'
        image[i, j] = np.clip(pixel_color.to_list(), 0, 1)

print("\rScanlines Remaining: ", end='')
print(blue("  0 "), end='')
print(green(f"|{'#' * (IMAGE_HEIGHT // 5)}| "), end='')
print(red("100.0%\t"), end='')
plt.imsave('image.png', image) # Saves image
