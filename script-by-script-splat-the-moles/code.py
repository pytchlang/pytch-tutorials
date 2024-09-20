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
            above_ground_time = random.uniform(0.5, 1.0)
            self.wait_seconds(above_ground_time)
            self.switch_costume("no-moles.png")
            under_ground_time = random.uniform(0.5, 1.0)
            self.wait_seconds(under_ground_time)

    @pytch.when_green_flag_clicked
    def init_score(self):
        self.score = 0
        self.show_variable("score")

    @pytch.when_key_pressed("j")
    def hit_left(self):
        if self.costume_number == 1:
            self.score += 1
            self.switch_costume("no-moles.png")
        else:
            self.score = 0
