from game.casting.solid import Solid
from game.shared.color import Color


class Ruby(Solid):
    """
    A simple ruby object. 

    The responsibility of a ruby is to fall from the sky give positive points.

    Attributes:
        _points (int): The number of points.
    """

    def __init__(self):
        # This is an inheritance
        super().__init__()
        self.set_points(10)
        self.set_color(Color(255, 0, 0))
        self.set_text("°")
