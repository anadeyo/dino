class Obstacle:
    def __init__(self, x: float, y: float, w: float, h: float) -> None:
        self.x = x
        self.y = y

        self.width = w 
        self.height = h 

    def display(self) -> None:
        pass


class Cactus(Obstacle):
    def __init__(self,x: float) -> None:
        super().__init__(x, 0.0, 100.0, 100.0)

class Bird(Obstacle):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, 100.0, 100.0)