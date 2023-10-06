"""
    Main
    @author Lehrman, Aidin
"""

import numpy as np
import matplotlib.pyplot as plt
from colors import red, green, blue
import math
from color import Color
from environment_variables import *
from hittable import HitRecord
from hittable_list import HittableList
from sphere import Sphere
from interval import Interval

def ray_color(ray: Ray3, world: HittableList):
    hit_record: HitRecord = HitRecord()
    if world.hit(ray, Interval(0, math.inf), hit_record):
        color = (hit_record.normal + Color(1, 1, 1)) / 2
        return color
    
    unit_direction: Vector3 = unit_vector(ray.direction)
    a: float = (unit_direction._y + 1) / 2
    color: Color = (Color(1, 1, 1) * (1 - a)) + (Color(0.5, 0.7, 1.0) * a)
    return color

# Image
ASPECT_RATIO: float = 16 / 9
IMAGE_WIDTH: int = 400  # Width of image

# Calculate the image height, and ensure that it's at least 1.
IMAGE_HEIGHT: int = int(IMAGE_WIDTH // ASPECT_RATIO)
IMAGE_HEIGHT = 1 if IMAGE_HEIGHT < 1 else IMAGE_HEIGHT

# Camera
FOCAL_LENGTH: float = 1.0
VIEWPORT_HEIGHT: float = 2.0
VIEWPORT_WIDTH: float = VIEWPORT_HEIGHT * (IMAGE_WIDTH / IMAGE_HEIGHT)
CAMERA_CENTER: Point3 = Point3(0, 0, 0)

# World
world: HittableList = HittableList()
world.add(Sphere(Point3(0, 0, -1), 0.5)) # Foreground
world.add(Sphere(Point3(0, -100, -1), 100)) # Background

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
    # Progress
    scanlines_remaining = IMAGE_HEIGHT - j
    completed_percent: int = math.floor(j / IMAGE_HEIGHT * 50)
    upcomming_percent: int = math.floor(50 - completed_percent)
    
    # Prints progress bar and percentage
    print("\rScanlines Remaining: ", end='')
    print(blue(
        f"{' ' * ( 3 - len(str(scanlines_remaining)))}{scanlines_remaining} "), end='')
    print(green(f"|{'■' * completed_percent}{' ' * upcomming_percent}| "), end='')
    print(red(f"{j / IMAGE_HEIGHT * 100:.2f}%\t"), end='')

    for i in range(IMAGE_WIDTH):  # For each pixel in each row
        # Get Point3 for position of center of pixel
        pixel_center: Point3 = PIXEL00_LOCATION + (PIXEL_DELTA_U * i) + (PIXEL_DELTA_V * j)
        
        # Get direction to pixel (Vector3)
        ray_direction: Vector3 = pixel_center - CAMERA_CENTER
        
        # Get Ray3 from camera center towards pixel center
        ray_to_pixel: Ray3 = Ray3(CAMERA_CENTER, ray_direction)
        
        # Gets pixel colors based on pixel's (x, y) values
        pixel_color = ray_color(ray_to_pixel, world)
        
        # Sets pixel color to 'pixel_color'
        image[j, i] = np.clip(pixel_color.to_list(), 0, 1)

# Print final progress bar
print("\rScanlines Remaining: ", end='')
print(blue("  0 "), end='')
print(green(f"|{'■' * 50}| "), end='')
print(red("100.0%\t"))

# Print message complete
print(green("RAY TRACING: Complete"))

plt.imsave('image.png', image)  # Saves image
