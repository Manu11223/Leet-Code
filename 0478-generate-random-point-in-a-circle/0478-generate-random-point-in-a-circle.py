import random

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.R = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        R = self.R
        while True:
            dx = random.uniform(-R, R)
            dy = random.uniform(-R, R)
            if dx * dx + dy * dy <= R * R:
                return [self.x + dx, self.y + dy]