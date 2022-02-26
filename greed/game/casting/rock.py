from game.casting.solid import Solid
from game.shared.color import Color


class Rock(Solid):
    """
    A simple rock object. 

    The responsibility of a rock is to fall from the sky give negative points.

    Attributes:
        _points (int): The number of points.
    """

    def __init__(self):
        # This is an inheritance
        super().__init__()
        self.set_points(-10)
        self.set_color(Color(109, 136, 141))
        self.set_text("■")
