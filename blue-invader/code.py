import pytch
import random


class Alien(pytch.Sprite):
    Costumes = ["enemy-alien.png", "friendly-alien.png"]

    @pytch.when_I_receive("make-clones")
    def make_clones(self):
        self.go_to_xy(-150, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(-90, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(-30, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(30, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(90, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(150, 180)

    @pytch.when_I_receive("play-game")
    def drift_down_screen(self):
        while True:
            self.switch_costume(random.choice([0, 1]))
            self.set_y(180)
            self.glide_to_xy(self.x_position, -180, 3.0)


class Galaxy(pytch.Stage):
    Backdrops = ["starry-sky.jpg"]

    @pytch.when_green_flag_clicked
    def run(self):
        pytch.broadcast_and_wait("make-clones")
        pytch.broadcast("play-game")
