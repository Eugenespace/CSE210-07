import random

from game.casting.actor import Actor
from game.shared.point import Point


class Solid(Actor):
    """
    A generic solid object class. 
    
    The responsibility of this class is to fall from the sky and provide points.

    Attributes:
        _points (int): The number of points.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.set_velocity(Point(0,5))
    
    def respawn(self):
        """
        Replace the object on the first line.
        """

        x = random.randint(1, 60 - 1)
        y = random.randint(0, 1)
        respawn_position = Point(x, y)
        respawn_position = respawn_position.scale(15)
        self.set_position(respawn_position)


    def get_points(self):
        """
        Gets the object points.
        
        Returns:
            int: The points.
        """
        return self._points

    def set_points(self, points):
        """
        Sets a value for the object points.
        
        Args:
            points (int): The given points.
        """
        self._points = points