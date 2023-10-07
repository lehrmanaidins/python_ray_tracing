"""
    Sphere Class
    @author Lehrman, Aidin
"""

import math
from hittable import Hittable, HitRecord
from environment_variables import Vector3, Point3, Ray3, dot
from interval import Interval
from material import Material

class Sphere(Hittable):
    def __init__(self, center: Point3, radius: float, material: Material) -> None:
        self.center: Point3 = center
        self.radius: float = radius
        self.material: Material = material

    def hit(self, ray: Ray3, ray_t: Interval, record: HitRecord) -> bool:
        oc: Vector3 = ray.origin - self.center
        a: float = ray.direction.length_squared()
        half_b: float = dot(oc, ray.direction)
        c: float = oc.length_squared() - (self.radius * self.radius)
        
        # Does ray hit Sphere?
        discriminant: float = (half_b * half_b) - (a * c)
        if (discriminant < 0):
            return False
        
        # Find nearest root that lies in the acceptable range
        sqrt_discriminant: float = math.sqrt(discriminant)
        root: float = (-half_b - sqrt_discriminant) / a
        if not ray_t.surrounds(root):
            root = (-half_b + sqrt_discriminant) / a
            if not ray_t.surrounds(root):
                return False

        record.set_t(root)
        record.set_point(ray.point_at(record.t))
        outward_normal: Vector3 = (record.point - self.center) / self.radius
        record.set_normal(ray, outward_normal)
        record.material = self.material
        
        return True