import pytch


class BunnyStage(pytch.Stage):
    Backdrops = [("world", "bunner-background.png")]


class Bunny(pytch.Sprite):
    Costumes = [
        ("up", "sit0.png"),
        ("right", "sit1.png"),
        ("down", "sit2.png"),
        ("left", "sit3.png"),
    ]

    start_shown = False

    @pytch.when_green_flag_clicked
    def go_to_starting_position(self):
        self.switch_costume("up")
        self.go_to_xy(0, -160)
        self.show()

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):
        self.switch_costume("up")
        if self.get_y() < 150:
            self.change_y(40)

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        self.switch_costume("right")
        if self.get_x() < 210:
            self.change_x(25)

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        self.switch_costume("down")
        if self.get_y() > -150:
            self.change_y(-40)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        self.switch_costume("left")
        if self.get_x() > -210:
            self.change_x(-25)
