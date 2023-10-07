"""
    Hittable Environment Objects
    @author Lehrman, Aidin
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from environment_variables import *
from color import Color
from interval import Interval
from material import Material

class HitRecord:
    def __init__(self) -> None:
        self.point: Point3 = Point3(0, 0, 0)
        self.normal: Vector3 = Vector3(0, 0, 0)
        self.material = Material(Color(0, 0, 0))
        self.front_face = False
        self.t: float = math.inf
        
    def set_t(self, t: float) -> None:
        self.t = t
        
    def set_point(self, point: Point3) -> None:
        self.point = point

    def copy(self, record: HitRecord) -> HitRecord:
        self.point = record.point
        self.normal = record.normal
        self.material = record.material
        self.t = record.t
        return self
        
    def set_normal(self, ray: Ray3, outward_normal: Vector3) -> None:
        self.front_face = dot(ray.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else outward_normal.negate()
        
    def set_material(self, material: Material) -> Material:
        self.material = material
        return self.material

class Hittable(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
        
    @abstractmethod
    def hit(self, ray: Ray3, ray_t: Interval, record: HitRecord) -> bool:
        print("Error: Abstract 'hit' function accessed.")
        return False