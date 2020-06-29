import pytch

import random


class BunnyStage(pytch.Stage):
    Backdrops = ["world.png"]


class Bunny(pytch.Sprite):
    Costumes = [ "up.png", "right.png", "down.png", "left.png"]

    @pytch.when_green_flag_clicked
    def go_to_starting_position(self):
        self.switch_costume("up")
        self.go_to_xy(0, -160)

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):
        self.switch_costume("up")
        if self.y_position < 150:
            self.change_y(40)

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        self.switch_costume("right")
        if self.x_position < 210:
            self.change_x(25)

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        self.switch_costume("down")
        if self.y_position > -150:
            self.change_y(-40)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        self.switch_costume("left")
        if self.x_position > -210:
            self.change_x(-25)


class Car(pytch.Sprite):
    Costumes = [
        ("left0", "car00.png"),
        ("right0", "car01.png"),
        ("left1", "car20.png"),
        ("right1", "car21.png"),
    ]

    @pytch.when_green_flag_clicked
    def start_hidden(self):
        self.hide()

    @pytch.when_green_flag_clicked
    def startTrafficRowOne(self):
        self.speed = 3
        while True:
            if random.random() < 0.2:
                self.go_to_xy(-285, -125)
                self.movement_direction = "right"
                pytch.create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @pytch.when_I_start_as_a_clone
    def drive(self):
        self.switch_costume(self.movement_direction + random.choice(["0", "1"]))
        self.set_size(0.65)
        self.show()
        if self.movement_direction == "right":
            while self.x_position < 285:
                self.change_x(self.speed)
        else:  # Direction should be "left"
            while self.x_position > -285:
                self.change_x(-self.speed)
        self.hide()
        self.delete_this_clone()

