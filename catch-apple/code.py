import pytch


class Bowl(pytch.Sprite):
    Costumes = ["bowl.png"]

    def move_with_keys(self):
        self.go_to_xy(0, -145)
