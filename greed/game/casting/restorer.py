from mimetypes import init
from game.shared.point import Point
import random

from game.casting.artifact import Artifact
from game.shared.color import Color
from game.shared.point import Point


class Restorer:
    """
    When a cast member is destroyed, the Restorer brings it back to life
    for unlimited gameplay.

    """

    def __init__(self):
        """
        Constructs the Restorer class with the following settings:
        _r,_g,_b = randomized red, green and blue values for randomized colors
        _x, _y = grid positional coordinates
        _position_start = position start
        _position = position start modifier

        _artifact = instantiates Artifact Parent Class
        _color = randomized colors
        _gray = static gray color
        """
        self._r = random.randint(0, 255)
        self._g = random.randint(0, 255)
        self._b = random.randint(0, 255)

        self._x = random.randint(1, 60 - 1)
        self._y = random.randint(0, 1)
        # The color and point here are inheritances
        self._position_start = Point(self._x, self._y)
        self._position = self._position_start.scale(15)

        self._artifact = Artifact()
        self._color = Color(self._r, self._g, self._b)
        self._gray = Color(129, 156, 161)

    def resurrect_artifact(self, cast):
        """
        resurrect_artifact takes cast and message and then gives parameters 
        for the creation of another artifact in the artifacts group.

        Args:
        cast: Receives the cast of actors
        message: Receives score 
        """
        self._artifact.set_text("*")
        self._artifact.set_font_size(25)
        self._artifact.set_color(self._color)
        self._artifact.set_position(self._position)
        cast.add_actor("artifacts", self._artifact)

    def resurrect_artifact2(self, cast):
        """
        resurrect_artifact2 takes cast and message and then gives parameters 
        for the creation of another artifact2 in the rocks group.

        Args:
        cast: Receives the cast of actors
        message: Receives score 
        """
        self._artifact.set_text("®")
        self._artifact.set_font_size(30)
        self._artifact.set_color(self._gray)
        self._artifact.set_position(self._position)
        cast.add_actor("rocks", self._artifact)
