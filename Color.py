"""
    Color Class
    @author Lehrman, Aidin
"""

from Vector3 import *

class Color(Vector3):
    def __str__(self) -> str:
        return f'{{{self.x}, {self.y}, {self.z}}}'

    def to_rgb(self) -> list:
        r: int = min(max(math.floor(self.x * 255.999), 0), 255) # [0, 255]
        g: int = min(max(math.floor(self.y * 255.999), 0), 255) # [0, 255]
        b: int = min(max(math.floor(self.z * 255.999), 0), 255) # [0, 255]
        return [r, g, b]
