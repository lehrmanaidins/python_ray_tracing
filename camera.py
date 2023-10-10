"""
    Camera Class
    @author Lehrman, Aidin
"""

import numpy as np
from numpy import float64, ndarray
import matplotlib.pyplot as plt
import math
import random
from colors import red, green, blue, yellow
from hittable_list import HittableList
from hittable import HitRecord
from environment_variables import Vector3, Point3, Ray3, random_unit_vector3
from color import Color, linear_to_gamma
from interval import Interval
from status import Status

class Camera:
    def __init__(self, aspect_ratio:float=1, image_width: int = 100) -> None:
        self.aspect_ratio: float = aspect_ratio
        self.image_width: int = image_width
        self.initialize()
    
    def render(self, world: HittableList, save_to_file: str='image.png') -> None:
        # Print message starting
        print(green('\nmain.py: Starting ...\n'))
        
        # Creates 2D array of [r, g, b] colors with width 'image_width' and height 'image_height'
        print(green('main.py: Creating Image ...'))
        print(yellow(f'\tHeight: {self.image_height}px\n\tWidth: {self.image_width}px\n'))
        image = np.zeros((self.image_height, self.image_width, 3))

        status: Status = Status(self.image_width, self.image_height)
        print(green('main.py: Rendering ...'))
        status.start()
        status.print_status(0)
        
        for j in range(self.image_height):  # For each row
            row_start_time: float = status.get_time()
            for i in range(self.image_width):  # For each pixel in each row
                pixel_color: Color = Color(0, 0, 0)
                for sample in range(self.samples_per_pixel):
                    ray: Ray3 = self.get_ray(i, j)
                    pixel_color += self.ray_color(ray, self.max_depth, world)
                self.write_color(image, i, j, pixel_color)
                
            row_end_time: float = status.get_time()
            status.set_rolling_average(row_end_time - row_start_time)
            status.print_status(j)
            
        status.print_status(self.image_height)

        # Print message complete
        print(green("\nmain.py: Render Complete\n"))
        
        plt.imsave(save_to_file, image)  # Saves image

    def initialize(self) -> None:
        # Calculate the image height, and ensure that it's at least 1.
        self.image_height: int = int(self.image_width // self.aspect_ratio)
        self.image_height = 1 if self.image_height < 1 else self.image_height

        self.center: Point3 = Point3(0, 0, 0)
        self.samples_per_pixel: int = 10
        self.max_depth = 50
        
        # Determine viewport dimensions
        focal_length: float = 1.0
        viewport_height: float = 2.0
        viewport_width: float = viewport_height * (self.image_width / self.image_height)

        # Calculate the vectors across the horizontal and down the vertical viewport edges.
        viewport_u = Vector3(viewport_width, 0, 0)
        viewport_v = Vector3(0, -viewport_height, 0)

        # Calculate the horizontal and vertical delta vectors from pixel to pixel.
        self.pixel_delta_u: Vector3 = viewport_u / self.image_width
        self.pixel_delta_v: Vector3 = viewport_v / self.image_height

        # Calculate the location of the upper left pixel.
        viewport_upper_left: Vector3 = \
            self.center - Vector3(0, 0, focal_length) - (viewport_u / 2) - (viewport_v / 2)
        self.pixel00_location: Vector3 = \
            viewport_upper_left + ((self.pixel_delta_u + self.pixel_delta_v) / 2)
            
    def get_ray(self, i: int, j: int) -> Ray3:
        # Get a randomly sampled camera ray for the pixel at location i,j.
        pixel_center: Point3 = self.pixel00_location + (self.pixel_delta_u * i) + (self.pixel_delta_v * j)
        pixel_sample: Point3 = pixel_center + self.pixel_sample_square()
        
        ray_origin: Point3 = self.center
        ray_direction: Vector3 = pixel_sample - ray_origin
        
        return Ray3(ray_origin, ray_direction)
    
    def pixel_sample_square(self) -> Point3:
        # Returns a random point in the square surrounding a pixel at the origin.
        px: float = -0.5 + random.random()
        py: float = -0.5 + random.random()
        return (self.pixel_delta_u * px) + (self.pixel_delta_v * py)
            
    def ray_color(self, ray: Ray3, depth: int, world: HittableList):
        hit_record: HitRecord = HitRecord()
        
        if depth <= 0:
            return Color(0, 0, 0)
        
        if world.hit(ray, Interval(0.001, math.inf), hit_record):
            scattered: Ray3 = Ray3()
            attenuation: Color = Color()
            if hit_record.material.scatter(ray, hit_record, attenuation, scattered):
                return attenuation * self.ray_color(scattered, depth - 1, world)

        unit_direction: Vector3 = ray.direction.unit_vector()
        a: float = (unit_direction._y + 1) / 2
        color: Color = (Color(1, 1, 1) * (1 - a)) + (Color(0.5, 0.7, 1.0) * a)
        return color
    
    
    def write_color(self, image: ndarray[float64], x: int, y: float, pixel_color: Color) -> None:
        r: float = pixel_color._x
        g: float = pixel_color._y
        b: float = pixel_color._z
        
        # Divide the color by the number of samples.
        scale: float = 1 / self.samples_per_pixel
        r *= scale
        b *= scale
        g *= scale
        
        # Apply the linear to gamma transform.
        r = linear_to_gamma(r)
        g = linear_to_gamma(g)
        b = linear_to_gamma(b)
        
        intensity: Interval = Interval(0, 0.999)
        color: Color = Color(intensity.clamp(r), intensity.clamp(g), intensity.clamp(b))
        image[y, x] = np.clip(color.to_list(), 0, 1)