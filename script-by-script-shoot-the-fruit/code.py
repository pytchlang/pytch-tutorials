import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["solid-green.png"]


class Fruit(pytch.Sprite):
    Costumes = ["apple.png"]

    @pytch.when_this_sprite_clicked
    def hit_fruit(self):
        pass
