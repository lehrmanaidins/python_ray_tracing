"""
    Color Class
    @author Lehrman, Aidin
"""

from Vector3 import *

class Color(Vector3):
    def __str__(self) -> str:
        return f'{{{self.x}, {self.y}, {self.z}}}'

    def to_rgb(self) -> list:
        r: int = min(max(math.floor(self.x * 255), 0), 255) # [0, 255]
        g: int = min(max(math.floor(self.y * 255), 0), 255) # [0, 255]
        b: int = min(max(math.floor(self.z * 255), 0), 255) # [0, 255]
        return [r, g, b]

    def to_list(self) -> list:
        r: float = min(max(self.x, 0), 1) # [0, 1]
        g: float = min(max(self.y, 0), 1) # [0, 1]
        b: float = min(max(self.z, 0), 1) # [0, 1]
        return [r, g, b]
