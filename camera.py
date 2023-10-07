"""
    Camera Class
    @author Lehrman, Aidin
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from colors import red, green, blue
from hittable_list import HittableList
from hittable import HitRecord
from environment_variables import Vector3, Point3, Ray3
from color import Color
from interval import Interval

class Camera:
    def __init__(self, aspect_ratio:float=1, image_width: int = 100) -> None:
        self.aspect_ratio: float = aspect_ratio
        self.image_width: int = image_width
    
    def render(self, world: HittableList) -> None:
        # Print message starting
        print(green("RAY TRACING: Starting"))
            
        self.initialize()
        
        # Creates 2D array of [r, g, b] colors with width 'image_width' and height 'image_height'
        image = np.zeros((self.image_height, self.image_width, 3))

        for j in range(self.image_height):  # For each row
            # Progress
            scanlines_remaining = self.image_height - j
            completed_percent: int = math.floor(j / self.image_height * 50)
            upcomming_percent: int = math.floor(50 - completed_percent)

            # Prints progress bar and percentage
            print("\rScanlines Remaining: ", end='')
            print(blue(f"{' ' * ( 3 - len(str(scanlines_remaining)))}{scanlines_remaining} "), end='')
            print(green(f"|{'■' * completed_percent}{' ' * upcomming_percent}| "), end='')
            print(red(f"{j / self.image_height * 100:.2f}%\t"), end='')

            for i in range(self.image_width):  # For each pixel in each row
                # Get Point3 for position of center of pixel
                pixel_center: Point3 = self.pixel00_location + (self.pixel_delta_u * i) + (self.viewport_v * j)

                # Get direction to pixel (Vector3)
                ray_direction: Vector3 = pixel_center - self.center

                # Get Ray3 from camera center towards pixel center
                ray_to_pixel: Ray3 = Ray3(self.center, ray_direction)

                # Gets pixel colors based on pixel's (x, y) values
                pixel_color = self.ray_color(ray_to_pixel, world)

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

    def initialize(self) -> None:
        # Calculate the image height, and ensure that it's at least 1.
        self.image_height: int = int(self.image_width // self.aspect_ratio)
        self.image_height = 1 if self.image_height < 1 else self.image_height

        self.center: Point3 = Point3(0, 0, 0)
        
        # Determine viewport dimensions
        self.focal_length: float = 1.0
        self.viewport_height: float = 2.0
        self.viewport_width: float = self.viewport_height * (self.aspect_ratio / self.image_height)

        # Calculate the vectors across the horizontal and down the vertical viewport edges.
        self.viewport_u = Vector3(self.viewport_width, 0, 0)
        self.viewport_v = Vector3(0, -self.viewport_height, 0)

        # Calculate the horizontal and vertical delta vectors from pixel to pixel.
        self.pixel_delta_u: Vector3 = self.viewport_u / self.image_width
        self.pixel_delta_v: Vector3 = self.viewport_v / self.image_height

        # Calculate the location of the upper left pixel.
        self.viewport_upper_left: Vector3 = self.center - \
            Vector3(0, 0, self.focal_length) - (self.viewport_u / 2) - (self.viewport_v / 2)
        self.pixel00_location = self.viewport_upper_left + \
            ((self.pixel_delta_u + self.pixel_delta_v) * 0.5)
            
    def ray_color(self, ray: Ray3, world: HittableList):
        hit_record: HitRecord = HitRecord()
        if world.hit(ray, Interval(0, math.inf), hit_record):
            color = (hit_record.normal + Color(1, 1, 1)) / 2
            return color

        unit_direction: Vector3 = ray.direction.unit_vector()
        a: float = (unit_direction._y + 1) / 2
        color: Color = (Color(1, 1, 1) * (1 - a)) + (Color(0.5, 0.7, 1.0) * a)
        return color