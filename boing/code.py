import pytch


class BoingBackground(pytch.Stage):
    Backdrops = ["table.png"]


class PlayerBat(pytch.Sprite):
    Costumes = ["player-normal.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-215, 0)

        while True:
            if pytch.key_pressed("w") and self.y_position < 117:
                self.change_y(3)
            if pytch.key_pressed("s") and self.y_position > -117:
                self.change_y(-3)


class RobotBat(pytch.Sprite):
    Costumes = ["robot-normal.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(215, 0)


class Ball(pytch.Sprite):
    Costumes = ["ball.png"]

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

            if self.x_position < -203:
                player_y = PlayerBat.the_original().y_position
                position_on_bat = self.y_position - player_y
                if (position_on_bat >= -45) and (position_on_bat <= 45):
                    y_speed = int(position_on_bat / 10)
                    self.change_x(-x_speed)
                    x_speed = -x_speed

            self.change_y(y_speed)

            if self.y_position > 158 or self.y_position < -158:
                self.change_y(-y_speed)
                y_speed = -y_speed
