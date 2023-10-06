"""
    Hittable List Class
    @author Lehrman, Aidin
"""

from hittable import Hittable, HitRecord
from typing import Union
from environment_variables import Vector3, Point3, Ray3

class HittableList(Hittable):
    def __init__(self) -> None:
        self.objects: list = []

    def clear(self) -> None:
        self.objects.clear()

    def add(self, object: Hittable) -> None:
        self.objects.append(object)

    def hit(self, ray: Ray3, rayt_min: float, rayt_max: float, record: HitRecord) -> bool:
        temp_record: HitRecord = HitRecord()
        hit_anything: bool = False
        closest_so_far: float = rayt_max

        for obj in self.objects:
            if obj.hit(ray, rayt_min, closest_so_far, temp_record):
                hit_anything = True
                closest_so_far = temp_record.t
                record.copy(temp_record)  # Update the record parameter with temp_record

        return hit_anything
