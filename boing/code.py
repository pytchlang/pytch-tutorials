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
            if pytch.key_is_pressed("w") and self.get_y() < 117:
                self.change_y(3)
            if pytch.key_is_pressed("s") and self.get_y() > -117:
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
        self.y_speed = 0
        while True:
            self.change_x(self.x_speed)

            if self.get_x() > 203:
                self.change_x(-self.x_speed)
                self.x_speed = -self.x_speed

            if self.get_x() < -203:
                player_y = PlayerBat.the_original().get_y()
                position_on_bat = self.get_y() - player_y
                if (position_on_bat >= -45) and (position_on_bat <= 45):
                    self.change_x(-self.x_speed)
                    self.x_speed = -self.x_speed
