"""
    Hittable Environment Objects
    @author Lehrman, Aidin
"""

from abc import ABC, abstractmethod
from environment_variables import *
from color import Color

class HitRecord:
    def __init__(self) -> None:
        self.point: Point3 = Point3(0, 0, 0)
        self.normal: Vector3 = Vector3(0, 0, 0)
        self.t: float = 0
        self.front_face: bool = False
        
    def set_face_normal(self, ray: Ray3, outward_normal: Vector3) -> None:
        self.front_face = dot(ray.direction, outward_normal) < 0
        self.normal: Vector3 = outward_normal if self.front_face else -outward_normal

class Hittable(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
        
    @abstractmethod
    def hit(ray: Ray3, rayt_min: float, rayt_max: float, record: HitRecord) -> bool:
        return False