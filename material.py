"""
    Abstract Material Class
    @author Lehrman, Aidin
"""

from color import Color
from environment_variables import Ray3, Vector3, random_unit_vector3, reflect

class HitRecord:
    pass

class Material():
    def __init__(self) -> None:
        pass
    
    def scatter(self, ray_in: Ray3, hit_record: HitRecord, attenuation: Color, scattered: Ray3) -> bool:
        return False
    
    
class Lambertian(Material):
    def __init__(self, a: Color) -> None:
        self.albedo = a
        
    def scatter(self, ray_in: Ray3, hit_record: HitRecord, attenuation: Color, scattered: Ray3) -> bool:
        scatter_direction: Vector3 = hit_record.normal + random_unit_vector3()
        
        # Catch degenerate scatter direction
        if scatter_direction.is_near_zero():
            scatter_direction = hit_record.normal
            
        scattered = Ray3(hit_record.point, scatter_direction)
        attenuation = self.albedo
        return True
    
class Metal(Material):
    def __init__(self, a: Color) -> None:
        self.albedo = a
        
    def scatter(self, ray_in: Ray3, hit_record: HitRecord, attenuation: Color, scattered: Ray3) -> bool:
        reflected: Vector3 = reflect(ray_in.direction.unit_vector, hit_record.normal)
        scattered = Ray3(hit_record.point, reflected)
        attenuation = self.albedo
        return True