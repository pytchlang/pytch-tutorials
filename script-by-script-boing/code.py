import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["court.png"]


class PlayerBat(pytch.Sprite):
    Costumes = ["player-bat-smile.png", "player-bat-wince.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        pass
