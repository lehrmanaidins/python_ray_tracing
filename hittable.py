"""
    Hittable Environment Objects
    @author Lehrman, Aidin
"""

from abc import ABC, abstractmethod
from environment_variables import *
from color import Color

class HitRecord:
    def __init__(self, point: Point3, normal: Vector3, t: float) -> None:
        self.point: Point3 = point
        self.normal: Vector3 = normal
        self.t: float = t

class Hittable(ABC):
    @abstractmethod
    def __init__(self, position: Point3, color: Color, ) -> None:
        self.position: Point3 = position
        self.color: Color = color
        
    @abstractmethod
    def hit(ray: Ray3, rayt_min: float, rayt_max: float, record: HitRecord) -> bool:
        return True