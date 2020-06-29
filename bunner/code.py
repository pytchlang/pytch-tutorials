import pytch

import random


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


class Car(pytch.Sprite):
    Costumes = [
        ("left0", "car00.png"),
        ("right0", "car01.png"),
        ("left1", "car20.png"),
        ("right1", "car21.png"),
    ]

    start_shown = False

    @pytch.when_green_flag_clicked
    def startTrafficRowOne(self):
        while True:
            if random.random() < 0.2:
                self.go_to_xy(-285, -125)
                self.direction = "right"
                pytch.create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @pytch.when_I_start_as_a_clone
    def drive(self):
        self.switch_costume(self.direction + random.choice(["0", "1"]))
        self.set_size(0.65)
        self.show()
        if self.direction == "right":
            while self.get_x() < 285:
                self.change_x( self.speed )

