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
