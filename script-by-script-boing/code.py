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
            if pytch.key_pressed("w") and self.y_position < 112:
                self.change_y(3)
            if pytch.key_pressed("s") and self.y_position > -112:
                self.change_y(-3)


class Ball(pytch.Sprite):
    Costumes = ["yellow-ball.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(0, 0)

        x_velocity = 3
