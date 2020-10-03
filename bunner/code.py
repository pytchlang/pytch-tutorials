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
