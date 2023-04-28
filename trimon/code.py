import pytch


class Background(pytch.Stage):
    Backdrops = ["blue-gradient.png"]


class LED1(pytch.Sprite):
    Costumes = ["light-off.png", "light-on.png"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(-140, 80)
