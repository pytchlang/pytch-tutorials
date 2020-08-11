import pytch
import random


class BoingBackground(pytch.Stage):
    Backdrops = ["table.png"]


class PlayerBat(pytch.Sprite):
    Costumes = ["player-normal.png", "player-flash.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-215, 0)

        while True:
            if pytch.key_pressed("w") and self.y_position < 117:
                self.change_y(3)
            if pytch.key_pressed("s") and self.y_position > -117:
                self.change_y(-3)

    @pytch.when_I_receive("player-hit")
    def flash_briefly(self):
        self.switch_costume("player-flash")
        pytch.wait_seconds(0.1)
        self.switch_costume("player-normal")


class RobotBat(pytch.Sprite):
    Costumes = ["robot-normal.png", "robot-flash.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(215, 0)

        while True:
            target_y = Ball.the_original().y_position
            if target_y < -117:
                target_y = -117
            if target_y > 117:
                target_y = 117
            self.set_y(target_y)

    @pytch.when_I_receive("robot-hit")
    def flash_briefly(self):
        self.switch_costume("robot-flash")
        pytch.wait_seconds(0.1)
        self.switch_costume("robot-normal")


class Ball(pytch.Sprite):
    Costumes = ["ball.png"]
    Sounds = ["hit.mp3", "bounce.mp3", "lost.mp3"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(0, 0)

        x_speed = 3
        y_speed = 0
        while True:
            self.change_x(x_speed)

            if self.x_position > 203:
                self.change_x(-x_speed)
                x_speed = -x_speed

                if y_speed == 0:
                    y_speed = random.choice([-1, 1])

                pytch.broadcast("robot-hit")
                self.start_sound("hit")

            if self.x_position < -203:
                player_y = PlayerBat.the_original().y_position
                position_on_bat = self.y_position - player_y
                if (position_on_bat >= -45) and (position_on_bat <= 45):
                    y_speed = int(position_on_bat / 10)
                    self.change_x(-x_speed)
                    x_speed = -x_speed
                    pytch.broadcast("player-hit")
                    self.start_sound("hit")
                else:
                    for i in range(10):
                        self.change_x(x_speed)
                        self.change_y(y_speed)
                    self.hide()
                    self.start_sound("lost")
                    break

            self.change_y(y_speed)

            if self.y_position > 158 or self.y_position < -158:
                self.change_y(-y_speed)
                y_speed = -y_speed
                self.start_sound("bounce")
