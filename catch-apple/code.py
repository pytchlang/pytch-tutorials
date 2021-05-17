import pytch
import random


class Bowl(pytch.Sprite):
    Costumes = ["bowl.png"]

    @pytch.when_green_flag_clicked
    def move_with_keys(self):
        self.go_to_xy(0, -145)

        while True:
            if pytch.key_pressed("a"):
                if self.x_position >= -145:
                    self.change_x(-2)
            if pytch.key_pressed("d"):
                if self.x_position <= 190:
                    self.change_x(2)


class Apple(pytch.Sprite):
    Costumes = []
