"""
    Sphere Class
    @author Lehrman, Aidin
"""

import math
from hittable import Hittable, HitRecord
from environment_variables import Vector3, Point3, Ray3, dot

class Sphere(Hittable):
    def __init__(self, position: Point3, radius: float) -> None:
        self.position: Point3 = position
        self.radius: float = radius

    def hit(self, ray: Ray3, rayt_min: float, rayt_max: float, record: HitRecord) -> bool:
        oc: Vector3 = ray.origin - self.position
        a: float = ray.direction.length_squared()
        half_b: float = dot(oc, ray.direction)
        c: float = oc.length_squared() - (self.radius * self.radius)
        
        discriminant: float = (half_b * half_b) - (a * c)
        if discriminant < 0:
            return False
        sqrt_discriminant: float = math.sqrt(discriminant)
        
        # Find nearest root that lies in the acceptable range
        root: float = (-half_b - sqrt_discriminant) / a
        if (root <= rayt_min or rayt_max <= root):
            root = (-half_b + sqrt_discriminant) / a
            if (root <= rayt_min or rayt_max <= root):
                return False
            
        record.t = root
        record.point = ray.point_at(record.t)
        outward_normal: Vector3 = (record.point - self.position) / self.radius
        record.set_face_normal(ray, outward_normal)
        
        return True