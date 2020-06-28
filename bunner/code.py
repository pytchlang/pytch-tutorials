import pytch


class BunnyStage(pytch.Stage):
    Backdrops = ["world.png"]


class Bunny(pytch.Sprite):
    Costumes = [ "up.png", "right.png", "down.png", "left.png"]

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
