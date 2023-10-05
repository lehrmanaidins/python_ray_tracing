"""
    Image Class
    @author Lehrman, Aidin
"""

import numpy as np
import matplotlib.pyplot as plt
from colors import red, green, blue
from Color import Color
from Vector3 import Vector3, Point3

# Image
ASPECT_RATIO: float = 1 / 1
IMAGE_WIDTH: int = 256  # Width of image

# Calculate the image height, and ensure that it's at least 1.
IMAGE_HEIGHT: int = int(IMAGE_WIDTH // ASPECT_RATIO)
IMAGE_HEIGHT = 1 if IMAGE_HEIGHT < 1 else IMAGE_HEIGHT

# Camera
FOCAL_LENGTH: float = 1
VIEWPORT_HEIGHT: float = 2
VIEWPORT_WIDTH: float = VIEWPORT_HEIGHT * (IMAGE_WIDTH / IMAGE_HEIGHT)
CAMERA_CENTER: Point3 = Point3(0, 0, 0)

# Calculate the vectors across the horizontal and down the vertical viewport edges.
VIEWPORT_U = Vector3(VIEWPORT_WIDTH, 0, 0)
VIEWPORT_V = Vector3(0, -VIEWPORT_HEIGHT, 0)

# Calculate the horizontal and vertical delta vectors from pixel to pixel.
PIXEL_DELTA_U: Vector3 = VIEWPORT_U / IMAGE_WIDTH
PIXEL_DELTA_V: Vector3 = VIEWPORT_V / IMAGE_HEIGHT

# Calculate the location of the upper left pixel.
VIEWPORT_UPPER_LEFT: Vector3 = CAMERA_CENTER - \
    Vector3(0, 0, FOCAL_LENGTH) - (VIEWPORT_U / 2) - (VIEWPORT_V / 2)
PIXEL00_LOCATION = VIEWPORT_UPPER_LEFT + \
    ((PIXEL_DELTA_U + PIXEL_DELTA_V) * 0.5)

# Creates 2D array of [r, g, b] colors with width 'image_width' and height 'image_height'
image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 3))

for j in range(IMAGE_HEIGHT):  # For each row
    # Calculates the amount of rows remaining
    scanlines_remaining = IMAGE_HEIGHT - j

    # Progress
    completed: int = j // 5
    upcomming: int = (IMAGE_HEIGHT // 5) - completed

    # Prints progress bar and percent
    print("\rScanlines Remaining: ", end='')
    print(blue(
        f"{' ' * ( 3 - len(str(scanlines_remaining)))}{scanlines_remaining} "), end='')
    print(green(f"|{'#' * completed}{' ' * upcomming}| "), end='')
    print(red(f"{j / IMAGE_HEIGHT * 100:.2f}%\t"), end='')

    for i in range(IMAGE_WIDTH):  # For each pixel in each row
        # Gets pixel colors based on pixel's (x, y) values
        pixel_color = Color(i / (IMAGE_WIDTH - 1), j / (IMAGE_HEIGHT - 1), 0)
        # Sets pixel color to 'pixel_color'
        image[i, j] = np.clip(pixel_color.to_list(), 0, 1)

print("\rScanlines Remaining: ", end='')
print(blue("  0 "), end='')
print(green(f"|{'#' * (IMAGE_HEIGHT // 5)}| "), end='')
print(red("100.0%\t"), end='')
plt.imsave('image.png', image)  # Saves image
