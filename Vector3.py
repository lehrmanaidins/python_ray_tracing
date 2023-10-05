"""
    Vector3 and Point3 Classes
    @author Lehrman, Aidin
"""

from __future__ import annotations
from typing import Union
import math

class Vector3:
    def __init__(self, *args: Union[int, float, Vector3]) -> None:
        if len(args) == 1:
            try:
                self.x: float = args[0].x
                self.y: float = args[0].y
                self.z: float = args[0].z
            except TypeError:
                pass
        elif len(args) == 3:
            try:
                self.x: float = args[0]
                self.y: float = args[1]
                self.z: float = args[2]
            except TypeError:
                pass
        else:
            raise TypeError
    
    def __str__(self) -> str:
        return f'[{self.x}, {self.y}, {self.z}]'
        
    def __add__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            x: float = self.x + value
            y: float = self.y + value
            z: float = self.z + value
            return Vector3(x, y, z)
        elif isinstance(value, Vector3):
            x: float = self.x + value.x
            y: float = self.y + value.y
            z: float = self.z + value.z
            return Vector3(x, y, z)
        else:
            raise TypeError
        
    def __iadd__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            self.x += value
            self.y += value
            self.z += value
            return self
        elif isinstance(value, Vector3):
            self.x += value.x
            self.y += value.y
            self.z += value.z
            return self
        else:
            raise TypeError
        
    def __sub__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            x: float = self.x - value
            y: float = self.y - value
            z: float = self.z - value
            return Vector3(x, y, z)
        elif isinstance(value, Vector3):
            x: float = self.x - value.x
            y: float = self.y - value.y
            z: float = self.z - value.z
            return Vector3(x, y, z)
        else:
            raise TypeError
        
    def __isub__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            self.x -= value
            self.y -= value
            self.z -= value
            return self
        elif isinstance(value, Vector3):
            self.x -= value.x
            self.y -= value.y
            self.z -= value.z
            return self
        else:
            raise TypeError
        
    def __mul__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            x: float = self.x * value
            y: float = self.y * value
            z: float = self.z * value
            return Vector3(x, y, z)
        elif isinstance(value, Vector3):
            x: float = self.x * value.x
            y: float = self.y * value.y
            z: float = self.z * value.z
            return Vector3(x, y, z)
        else:
            raise TypeError
        
    def __imul__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            self.x *= value
            self.y *= value
            self.z *= value
            return self
        elif isinstance(value, Vector3):
            self.x *= value.x
            self.y *= value.y
            self.z *= value.z
            return self
        else:
            raise TypeError
        
    def __truediv__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            try:
                x: float = self.x / value
                y: float = self.y / value
                z: float = self.z / value
                return Vector3(x, y, z)
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        elif isinstance(value, Vector3):
            try:
                x: float = self.x / value.x
                y: float = self.y / value.y
                z: float = self.z / value.z
                return Vector3(x, y, z)
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        else:
            raise TypeError
        
    def __itruediv__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            try:
                self.x /= value
                self.y /= value
                self.z /= value
                return self
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        elif isinstance(value, Vector3):
            try:
                self.x /= value.x
                self.y /= value.y
                self.z /= value.z
                return self
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        else:
            raise TypeError
        
    def __floordiv__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            try:
                x: float = self.x // value
                y: float = self.y // value
                z: float = self.z // value
                return Vector3(x, y, z)
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        elif isinstance(value, Vector3):
            try:
                x: float = self.x // value.x
                y: float = self.y // value.y
                z: float = self.z // value.z
                return Vector3(x, y, z)
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        else:
            raise TypeError
        
    def __ifloordiv__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            try:
                self.x //= value
                self.y //= value
                self.z //= value
                return self
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        elif isinstance(value, Vector3):
            try:
                self.x //= value.x
                self.y //= value.y
                self.z //= value.z
                return self
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        else:
            raise TypeError
    
    def length_squared(self) -> float:
        return (self.x ** 2) + (self.y ** 2) + (self.z ** 2)
    
    def length(self) -> float:
        return math.sqrt(self.length_squared())
    
"""
    Point Class is used for readability (It is a Vector3, just different name)
"""
class Point3(Vector3):
    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

    
"""
    Vector Utility Functions
"""
def dot(a: Vector3, b: Vector3) -> float:
    return (a.x * b.x) + (a.y * b.y) + (a.z * b.z)

def cross(a: Vector3, b: Vector3) -> Vector3:
    return Vector3(a.y * b.z - a.z * b.y,
                   a.z * b.x - a.x * b.z,
                   a.x * b.y - a.y * b.x)

def unit_vector(a: Vector3) -> Vector3:
    return a / a.length()
