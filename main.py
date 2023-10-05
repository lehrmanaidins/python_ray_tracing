"""
    Image Class
    @author Lehrman, Aidin
"""

import numpy as np
import matplotlib.pyplot as plt
from Color import *
from Vector3 import *

# Image
image_height = 256
image_width = 256
image = np.zeros((image_height, image_width, 3))

for j in range(image_height):
    
    scanlines_remaining = image_height - j
    # Print no new line (fix)
    print(f"\rScanlines Remaining:\t{' ' * ( 3 - len(str(scanlines_remaining)))}{scanlines_remaining}\t{j / image_height * 100:.2f}%")
    
    for i in range(image_width):
        
        pixel_color = Color(i / (image_width - 1), j / (image_height - 1), 0)
        image[i, j] = np.clip([pixel_color.x, pixel_color.y, pixel_color.z], 0, 1)


plt.imsave('image.png', image)
