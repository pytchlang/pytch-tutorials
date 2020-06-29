import pytch

import random


class BunnyStage(pytch.Stage):
    Backdrops = ["world.png"]


class Bunny(pytch.Sprite):
    Costumes = [ "up.png", "right.png", "down.png", "left.png"]

    start_shown = False

    @pytch.when_green_flag_clicked
    def go_to_starting_position(self):
        self.switch_costume("up")
        self.go_to_xy(0, -160)
        self.show()

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):
        self.switch_costume("up")
        if self.y_position < 150:
            self.change_y(40)

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        self.switch_costume("right")
        if self.x_position < 210:
            self.change_x(25)

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        self.switch_costume("down")
        if self.y_position > -150:
            self.change_y(-40)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        self.switch_costume("left")
        if self.x_position > -210:
            self.change_x(-25)


class Car(pytch.Sprite):
    Costumes = [
        ("left0", "car00.png"),
        ("right0", "car01.png"),
        ("left1", "car20.png"),
        ("right1", "car21.png"),
    ]

    start_shown = False
