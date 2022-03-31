import pytch
import random


class Alien(pytch.Sprite):
    Costumes = ["enemy-alien.png", "friendly-alien.png"]

    @pytch.when_green_flag_clicked
    def drift_down_screen(self):
        while True:
            self.switch_costume(random.choice([0, 1]))
            self.set_y(180)
            self.glide_to_xy(self.x_position, -180, 3.0)


class Galaxy(pytch.Stage):
    Backdrops = ["starry-sky.jpg"]
