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

        while True:
            costume_index = random.randint(1, 3)
            self.switch_costume(costume_index)
