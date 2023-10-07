"""
    Abstract Material Class
    @author Lehrman, Aidin
"""

from __future__ import annotations
from color import Color
from environment_variables import Ray3, Vector3, random_unit_vector3, reflect, dot

class Material():
    def __init__(self, albedo: Color) -> None:
        self.albedo = albedo

    def __str__(self) -> str:
        return str(self.albedo)
    
    def scatter(self, ray_in: Ray3, hit_record, attenuation: Color, scattered: Ray3) -> bool:
        return False
    
    
class Lambertian(Material):
    def __init__(self, albedo: Color) -> None:
        self.albedo = albedo

        
    def scatter(self, ray_in: Ray3, hit_record, attenuation: Color, scattered: Ray3) -> bool:
        scatter_direction: Vector3 = hit_record.normal + random_unit_vector3()
        
        # Catch degenerate scatter direction
        if scatter_direction.is_near_zero():
            scatter_direction = hit_record.normal
            
        scattered.copy(Ray3(hit_record.point, scatter_direction))
        attenuation.copy(self.albedo)
        return True
    
class Metal(Material):
    def __init__(self, albedo: Color, fuzz: float) -> None:
        self.albedo = albedo

        self.fuzz = fuzz if fuzz < 1 else 1
        
    def scatter(self, ray_in: Ray3, hit_record, attenuation: Color, scattered: Ray3) -> bool:
        reflected: Vector3 = reflect(ray_in.direction.unit_vector(), hit_record.normal)
        scattered.copy(Ray3(hit_record.point, reflected + (random_unit_vector3() * self.fuzz)))
        attenuation.copy(self.albedo)
        return (dot(scattered.direction, hit_record.normal) > 0)