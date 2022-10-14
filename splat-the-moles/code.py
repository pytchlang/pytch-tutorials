import pytch


class Field(pytch.Stage):
    Backdrops = ["green-field.jpg"]


class Mole(pytch.Sprite):
    Costumes = [
        "all-empty.png",
        "left-mole.png",
        "centre-mole.png",
        "right-mole.png",
    ]

    @pytch.when_green_flag_clicked
    def pop_up_and_down(self):
        self.go_to_xy(0, -70)
