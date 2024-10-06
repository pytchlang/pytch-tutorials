import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["solid-green.png"]

    @pytch.when_green_flag_clicked
    def setup(self):
        pass


class Fruit(pytch.Sprite):
    Costumes = ["apple.png"]

    @pytch.when_this_sprite_clicked
    def hit_fruit(self):
        self.hide()
        pytch.wait_seconds(1)

        appear_x = random.randint(-200, 200)
        appear_y = random.randint(-140, 140)
        self.go_to_xy(appear_x, appear_y)

        self.show()
