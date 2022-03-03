import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["leafy-background.png"]

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
    Costumes = [
        "Apple-1.png",
        "Apple-2.png",
        "Apple-3.png",
        "Apple-4.png",
        "GoldApple-1.png",
        "Lemon-1.png",
        "Lemon-2.png",
        "Lemon-3.png",
        "Lemon-4.png",
        "Orange-1.png",
        "Orange-2.png",
        "Orange-3.png",
        "Orange-4.png",
        "Strawberry-1.png"
    ]

    @pytch.when_green_flag_clicked
    def init_size(self):
        self.set_size(0.25)

    @pytch.when_this_sprite_clicked
    def hit_fruit(self):
        self.hide()

        Stage.score += 1

        pytch.wait_seconds(1)

        appear_x = random.randint(-200, 200)
        appear_y = random.randint(-140, 140)
        self.go_to_xy(appear_x, appear_y)

        new_costume = random.choice(
            ["Apple-1.png", "Orange-1.png"]
        )

        self.show()
