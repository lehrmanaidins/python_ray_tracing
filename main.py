"""
    Main
    @author Lehrman, Aidin
"""

from camera import Camera
from hittable_list import HittableList
from environment_variables import Point3
from sphere import Sphere
from color import Color
from material import Lambertian, Metal, Dielectric

material_ground: Lambertian = Lambertian(Color(0.8, 0.8, 0.0))
material_center: Lambertian = Lambertian(Color(0.1, 0.2, 0.5))
material_left: Dielectric = Dielectric(1.5)
material_right: Metal = Metal(Color(0.8, 0.6, 0.2), 0.0)

# World
world: HittableList = HittableList()
world.add(Sphere(Point3(0, -100.5, -1), 100, material_ground)) # Background
world.add(Sphere(Point3(0, 0, -1), 0.5, material_center))
# world.add(Sphere(Point3(-1, 0, -1), 0.5, material_left))
# world.add(Sphere(Point3(1, 0, -1), 0.5, material_right))

aspect_ratio: float = 16 / 9
image_width: int = int(1080)
camera: Camera = Camera(aspect_ratio, image_width)
camera.samples_per_pixel = 100
camera.max_depth = 50

camera.render(world, 'render_2560px1440p_100_samples_per_pixel.png')