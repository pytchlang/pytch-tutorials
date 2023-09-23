import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["solid-white.png"]


class Bowl(pytch.Sprite):
    Costumes = ["Bowl-1.png", "Bowl-2.png"]

    @pytch.when_green_flag_clicked
    def move_with_keys(self):
        pass
