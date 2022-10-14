import pytch
import random


class Field(pytch.Stage):
    Backdrops = ["green-field.jpg"]


class Mole(pytch.Sprite):
    Costumes = [
        "all-empty.png",
        "left-mole.png",
        "centre-mole.png",
        "right-mole.png",
    ]
    Sounds = ["splat.mp3", "thud.mp3"]

    @pytch.when_green_flag_clicked
    def pop_up_and_down(self):
        self.go_to_xy(0, -70)

        while True:
            self.switch_costume(random.randint(1, 3))
            pytch.wait_seconds(random.uniform(0.5, 1.0))
            self.switch_costume("all-empty")
            pytch.wait_seconds(random.uniform(0.5, 1.0))

    @pytch.when_green_flag_clicked
    def set_up_scoring(self):
        self.score = 0
        pytch.show_variable(self, "score")

    @pytch.when_key_pressed("j")
    def hit_left(self):
        if self.costume_number == 1:
            self.score += 1
            self.switch_costume("all-empty")
        else:
            self.score = 0
