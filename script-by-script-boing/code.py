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
            if self.key_pressed("w") and self.y_position < 112:
                self.change_y(3)
            if self.key_pressed("s") and self.y_position > -112:
                self.change_y(-3)


class RobotBat(pytch.Sprite):
    Costumes = ["robot-bat-smile.png", "robot-bat-wince.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(212, 0)

        while True:
            target_y = Ball.y_position
            self.set_y(target_y)


class Ball(pytch.Sprite):
    Costumes = ["yellow-ball.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(0, 0)

        x_velocity = 3
        y_velocity = 0
        while True:
            self.change_x(x_velocity)

            if self.x_position > 195:
                self.change_x(-x_velocity)
                x_velocity = -x_velocity
                y_velocity = random.randint(-4, 4)

            if self.x_position < -195:
                if self.touching(PlayerBat):
                    self.change_x(-x_velocity)
                    x_velocity = -x_velocity
                    y_velocity = random.randint(-4, 4)
                else:
                    self.hide()
                    break

            self.change_y(y_velocity)

            if self.y_position > 150 or self.y_position < -150:
                self.change_y(-y_velocity)
                y_velocity = -y_velocity
