"""
    Hittable List Class
    @author Lehrman, Aidin
"""

from hittable import Hittable, HitRecord
from environment_variables import Vector3, Point3, Ray3
from interval import Interval

class HittableList(Hittable):
    def __init__(self) -> None:
        self.objects: list[Hittable] = []

    def clear(self) -> None:
        self.objects.clear()

    def add(self, object: Hittable) -> None:
        self.objects.append(object)

    def hit(self, ray: Ray3, ray_t: Interval, record: HitRecord) -> bool:
        temp_record: HitRecord = HitRecord()
        hit_anything: bool = False
        closest_so_far: float = ray_t.max

        for object in self.objects:
            if object.hit(ray, Interval(ray_t.min, closest_so_far), temp_record):
                hit_anything = True
                closest_so_far = temp_record.t
                record.copy(temp_record)  # Update the record parameter with temp_record

        return hit_anything
