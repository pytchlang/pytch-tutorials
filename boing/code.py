import pytch


class BoingBackground(pytch.Stage):
    Backdrops = [
        ('boing', 'images/table.png'),
    ]


class PlayerBat(pytch.Sprite):
    Costumes = [
        ('normal', 'images/bat00.png', 60, 60),
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


class Ball(pytch.Sprite):
    Costumes = [
        ('ball', 'images/ball.png', 12, 12),
    ]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(0, 0)
        self.show()

        while True:
            self.change_x(3)
