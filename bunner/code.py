import pytch

import random


WAITING, PLAYING, SQUISHED = range(3)


class BunnyStage(pytch.Stage):
    Backdrops = [("world", "bunner-background.png")]


class Bunny(pytch.Sprite):
    Costumes = [
        ("up", "sit0.png"),
        ("right", "sit1.png"),
        ("down", "sit2.png"),
        ("left", "sit3.png"),
        ("up_squished", "splat0.png"),
        ("right_squished", "splat1.png"),
        ("down_squished", "splat2.png"),
        ("left_squished", "splat3.png"),
    ]

    start_shown = False

    @pytch.when_green_flag_clicked
    def go_to_starting_position(self):
        self.switch_costume("up")
        self.go_to_xy(0, -160)
        self.mode = WAITING
        self.hide()
        self.lives = -1

    @pytch.when_green_flag_clicked
    def start_game(self):
        self.lives = 3
        self.switch_costume("up")
        self.go_to_xy(0, -160)
        self.mode = PLAYING
        self.show()

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):
        if self.mode == PLAYING:
            self.switch_costume("up")
            if self.get_y() < 150:
                self.change_y(40)

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        if self.mode == PLAYING:
            self.switch_costume("right")
            if self.get_x() < 210:
                self.change_x(25)

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        if self.mode == PLAYING:
            self.switch_costume("down")
            if self.get_y() > -150:
                self.change_y(-40)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        if self.mode == PLAYING:
            self.switch_costume("left")
            if self.get_x() > -210:
                self.change_x(-25)

    @pytch.when_I_receive("squish bunny")
    def squish(self):
        if self.mode != SQUISHED:
            self.mode = SQUISHED
            self.switch_costume(self.costume_name + "_squished")
            pytch.wait_seconds(0.5)
            self.start_game()


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
        self.speed = 3
        while True:
            if random.random() < 0.2:
                self.go_to_xy(-285, -125)
                self.direction = "right"
                pytch.create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @pytch.when_green_flag_clicked
    def startTrafficRowTwo(self):
        self.speed = 3
        while True:
            if random.random() < 0.2:
                self.go_to_xy(285, -80)
                self.direction = "left"
                pytch.create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @pytch.when_green_flag_clicked
    def startTrafficRowThree(self):
        self.speed = 3
        while True:
            if random.random() < 0.2:
                self.go_to_xy(-285, -30)
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
        else: # Direction should be "left"
            while self.get_x() > -285:
                self.change_x( -self.speed )
        self.hide()
        self.delete_this_clone()

    @pytch.when_I_start_as_a_clone
    def check_for_collision(self):
        while True:
            while not self.hits(Bunny.the_original()):
                pass
            pytch.broadcast("squish bunny")

    def hits(self, other):
        return (abs(self.get_y() - other.get_y()) <= 10 and
                abs(self.get_x() - other.get_x()) <= 40)
