import pytch


class Bowl(pytch.Sprite):
    Costumes = ["bowl.png"]

    @pytch.when_green_flag_clicked
    def move_with_keys(self):
        self.go_to_xy(0, -145)

        while True:
            if pytch.key_is_pressed("d"):
                if self.get_x() <= 190:
                    self.change_x(2)
