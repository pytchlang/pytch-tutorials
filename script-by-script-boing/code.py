import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["table.png"]


class PlayerBat(pytch.Sprite):
    Costumes = ["player-normal.png", "player-flash.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-215, 0)

        while True:
            if pytch.key_pressed("w") and self.y_position < 120:
                self.change_y(3)
            if pytch.key_pressed("s") and self.y_position > -120:
                self.change_y(-3)


class RobotBat(pytch.Sprite):
    Costumes = ["robot-normal.png", "robot-flash.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(215, 0)


class Ball(pytch.Sprite):
    Costumes = ["ball.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(0, 0)

        x_velocity = 3
        while True:
            self.change_x(x_velocity)

            if self.x_position > 200:
                self.change_x(-x_velocity)
                x_velocity = -x_velocity

            if self.x_position < -200:
                if self.touching(PlayerBat):
                    self.change_x(-x_velocity)
                    x_velocity = -x_velocity
