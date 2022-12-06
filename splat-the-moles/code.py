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
            chosen_costume_number = random.randint(1, 3)
            self.switch_costume(chosen_costume_number)
            gpio_pin = 21 + chosen_costume_number
            pytch.wait_seconds(random.uniform(0.5, 1.0))
            self.switch_costume("all-empty")
            pytch.wait_seconds(random.uniform(0.5, 1.0))

    @pytch.when_green_flag_clicked
    def set_up_scoring(self):
        self.score = 0
        pytch.show_variable(self, "score")

    @pytch.when_gpio_goes_low(16)
    def hit_left(self):
        if self.costume_number == 1:
            self.start_sound("splat")
            self.score += 1
            self.switch_costume("all-empty")
        else:
            self.start_sound("thud")
            self.score = 0

    @pytch.when_gpio_goes_low(20)
    def hit_centre(self):
        if self.costume_number == 2:
            self.start_sound("splat")
            self.score += 1
            self.switch_costume("all-empty")
        else:
            self.start_sound("thud")
            self.score = 0

    @pytch.when_gpio_goes_low(21)
    def hit_right(self):
        if self.costume_number == 3:
            self.start_sound("splat")
            self.score += 1
            self.switch_costume("all-empty")
        else:
            self.start_sound("thud")
            self.score = 0
