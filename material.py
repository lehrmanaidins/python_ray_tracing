"""
    Abstract Material Class
    @author Lehrman, Aidin
"""

from __future__ import annotations
import math
from color import Color
from environment_variables import Point3, Ray3, Vector3, random_unit_vector3, reflect, dot, unit_vector, refract

class Material():
    def __init__(self, albedo: Color) -> None:
        self.albedo = albedo

    def __str__(self) -> str:
        return f'{type(self)}'
    
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
        self.albedo: Color = albedo
        self.fuzz: float = fuzz if fuzz < 1 else 1
        
    def scatter(self, ray_in: Ray3, hit_record, attenuation: Color, scattered: Ray3) -> bool:
        reflected: Vector3 = reflect(ray_in.direction.unit_vector(), hit_record.normal)
        scattered.copy(Ray3(hit_record.point, reflected + (random_unit_vector3() * self.fuzz)))
        attenuation.copy(self.albedo)
        return (dot(scattered.direction, hit_record.normal) > 0)
    
class Dielectric(Material):
    def __init__(self, index_of_refraction: float) -> None:
        self.index_of_refraction = index_of_refraction
        
    def scatter(self, ray_in: Ray3, hit_record, attenuation: Color, scattered: Ray3) -> bool:
        attenuation.copy(Color(1, 1, 1))
        refraction_ratio: float = (1 / self.index_of_refraction) if hit_record.front_face else self.index_of_refraction
        
        unit_direction: Vector3 = unit_vector(ray_in.direction)
        cos_theta: float = min(dot(unit_direction * -1, hit_record.normal), 1)
        sin_theta: float = math.sqrt(1 - (cos_theta * cos_theta))
        
        cannot_refract: bool = refraction_ratio * sin_theta > 1
        direction: Vector3 = Vector3()
        
        if cannot_refract:
            direction = reflect(unit_direction, hit_record.normal)
        else:
            direction = refract(unit_direction, hit_record.normal, refraction_ratio)
        
        scattered.copy(Ray3(Point3(hit_record.point), direction))
        return True