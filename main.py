"""
    Main
    @author Lehrman, Aidin
"""

from camera import Camera
from hittable_list import HittableList
from environment_variables import Point3
from sphere import Sphere

# World
world: HittableList = HittableList()
world.add(Sphere(Point3(0, 0, -1), 0.5)) # Foreground
world.add(Sphere(Point3(0, -100.5, -1), 100)) # Background

aspect_ratio: float = 16 / 9
image_width: int = int(400)
camera: Camera = Camera(aspect_ratio, image_width)
camera.samples_per_pixel = 100
camera.max_depth = 50

camera.render(world)