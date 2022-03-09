import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Trail(Actor):
    """
    A trail item that snakes leave behind.
    
    The responsibility of Trail is to add to trail length by position and points that it's worth.

    Attributes:
        _points (int): The number of points the trail is worth.
    """
    def __init__(self):
        "Constructs a new trail."
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the trail left behind is worth."""
        self._points = 5
        # x = random.randint(1, constants.COLUMNS - 1)
        # y = random.randint(1, constants.ROWS - 1)
        # position = Point(x, y)
        # position = position.scale(constants.CELL_SIZE)
        # self.set_position(position)
        
    def get_points(self):
        """Gets the points the trail is worth.
        
        Returns:
            points (int): The points the trail is worth.
        """
        return self._points