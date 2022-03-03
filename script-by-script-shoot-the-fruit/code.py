import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["solid-green.png"]

    @pytch.when_green_flag_clicked
    def setup(self):
        Stage.score = 0
        pytch.show_variable(Stage, "score")

    @pytch.when_stage_clicked
    def missed_fruit(self):
        Stage.score -= 5
        if Stage.score < 0:
            Stage.score = 0


class Fruit(pytch.Sprite):
    Costumes = ["apple.png", "orange.png"]

    @pytch.when_this_sprite_clicked
    def hit_fruit(self):
        self.hide()

        Stage.score += 1

        pytch.wait_seconds(1)

        appear_x = random.randint(-200, 200)
        appear_y = random.randint(-140, 140)
        self.go_to_xy(appear_x, appear_y)

        self.show()
