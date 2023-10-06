"""
    Sphere Class
    @author Lehrman, Aidin
"""

import math
from hittable import Hittable, HitRecord
from environment_variables import Vector3, Point3, Ray3, dot
from interval import Interval

class Sphere(Hittable):
    def __init__(self, position: Point3, radius: float) -> None:
        self.position: Point3 = position
        self.radius: float = radius

    def hit(self, ray: Ray3, ray_t: Interval, record: HitRecord) -> bool:
        oc: Vector3 = ray.origin - self.position
        a: float = ray.direction.length_squared()
        half_b: float = dot(oc, ray.direction)
        c: float = oc.length_squared() - (self.radius * self.radius)
        
        # Does ray hit Sphere?
        discriminant: float = (half_b * half_b) - (a * c)
        if discriminant < 0:
            return False
        
        # Find nearest root that lies in the acceptable range
        sqrt_discriminant: float = math.sqrt(discriminant)
        root: float = (-half_b - sqrt_discriminant) / a
        if not ray_t.surrounds(root):
            root = (-half_b + sqrt_discriminant) / a
            if not ray_t.surrounds(root):
                return False
            
        record.t = root
        record.point = ray.point_at(record.t)
        outward_normal: Vector3 = (record.point - self.position) / self.radius
        record.set_face_normal(ray, outward_normal)
        
        return True