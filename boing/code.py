import pytch


class BoingBackground(pytch.Stage):
    Backdrops = ["table.png"]


class PlayerBat(pytch.Sprite):
    Costumes = [
        ("normal", "bat00.png"),
    ]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-215, 0)
        self.show()

        while True:
            if pytch.key_pressed("w") and self.y_position < 117:
                self.change_y(3)
            if pytch.key_pressed("s") and self.y_position > -117:
                self.change_y(-3)


class RobotBat(pytch.Sprite):
    Costumes = [
        ("normal", "bat10.png"),
    ]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(215, 0)
        self.show()


class Ball(pytch.Sprite):
    Costumes = ["ball.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(0, 0)
        self.show()

        self.x_speed = 3
        while True:
            self.change_x(self.x_speed)

            if self.x_position > 203:
                self.change_x(-self.x_speed)
                self.x_speed = -self.x_speed

            if self.x_position < -203:
                player_y = PlayerBat.the_original().y_position
                position_on_bat = self.y_position - player_y
                if (position_on_bat >= -45) and (position_on_bat <= 45):
                    self.change_x(-self.x_speed)
                    self.x_speed = -self.x_speed
