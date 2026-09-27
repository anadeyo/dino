class Dino: 
    def __init__(self) -> None:
        self.y = ...
        self.vy = 0.0

        self.running = False
        self.ducking = False
        self.is_dead = False


    def jump(self) -> None:
        pass

    def die(self) -> None:
        self.is_dead = True

    def duck(self, is_active: bool) -> None:
        self.ducking = is_active

    def display(self) -> None:
        pass