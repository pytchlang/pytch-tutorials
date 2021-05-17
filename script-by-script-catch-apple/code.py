import pytch
import random
import math


class Stage(pytch.Stage):
    Backdrops = ["solid-white.png"]


class Bowl(pytch.Sprite):
    Costumes = ["Bowl-1.png", "Bowl-2.png"]

    @pytch.when_green_flag_clicked
    def move_with_keys(self):
        self.set_size(0.3)
        self.go_to_xy(0, -145)

        while True:
            if self.key_pressed("a"):
                if self.x_position > -145:
                    self.change_x(-2)
            if self.key_pressed("d"):
                if self.x_position < 190:
                    self.change_x(2)


class Apple(pytch.Sprite):
    Costumes = [
        "Apple-1.png",
        "Apple-2.png",
        "Apple-3.png",
        "Apple-4.png",
        "GoldApple-1.png",
        "Lemon-1.png",
        "Lemon-2.png",
        "Lemon-3.png",
        "Lemon-4.png",
        "Orange-1.png",
        "Orange-2.png",
        "Orange-3.png",
        "Orange-4.png",
        "Strawberry-1.png"
    ]

    @pytch.when_green_flag_clicked
    def move_down_stage(self):
        self.set_size(0.25)
        self.go_to_xy(100, 200)
        while self.y_position > -140:
            self.change_y(-3)
            if self.touching(Bowl):
                self.hide()


class ScoreKeeper(pytch.Sprite):
    Costumes = []
