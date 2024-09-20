import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["cartoon-field.png"]


class Mole(pytch.Sprite):
    Costumes = ["no-moles.png", "mole-left.png", "mole-centre.png", "mole-right.png"]

    @pytch.when_green_flag_clicked
    def run(self):
        self.go_to_xy(0, -100)
