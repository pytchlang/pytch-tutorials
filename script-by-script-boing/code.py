import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["court.png"]


class PlayerBat(pytch.Sprite):
    Costumes = ["player-bat-smile.png", "player-bat-wince.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-212, 0)

        while True:
            if self.key_pressed("w"):
                self.change_y(3)
