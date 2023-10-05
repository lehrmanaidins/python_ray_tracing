"""
    Ray Class
    @author Lehrman, Aidin

"""

from Vector3 import *

class Ray3:
    """ Ray3 is made up of two parts; a point in 3D space, and a vector in a direction
    
    Args:
        origin (Point3): Origin point of the ray
        direction (Vector3): Direction the ray is pointing towards

    Returns:
        3D Ray from Point3 'origin' in direction 'direction' with infinite magnitude
    
    """
    def __init__(self, origin: Point3, direction: Vector3) -> None:
        if not (isinstance(origin, Vector3) and isinstance(direction, Vector3)):
            raise TypeError
        self.origin = origin
        self.direction = direction

    def __str__(self) -> str:
        return f'{str(self.origin)} -> {str(self.direction)}'
    
    def at(self, t: float) -> Point3:
        """ Returns point that is on ray 't' distance from ray's origin
        :t: Distance from origin
        :t type: float or int
        :returns: Point3 on ray 't' distnace from origin
        :rtype: Point3
        """
        if not (isinstance(t, float) or isinstance(t, int)):
            raise TypeError
        return self.origin + (self.direction * t)
    