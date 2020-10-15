import pytch


class Background(pytch.Stage):
    Backdrops = ["background.png"]


class Block(pytch.Sprite):
    Costumes = ["block0.png", "block1.png"]
    start_shown = False

    @pytch.when_green_flag_clicked
    def create_pyramid(self):
        for r in range(7):
            for b in range(7 - r):
                self.go_to_xy(-150 + (b * 56) + (r * 28),
                              -145 + (r * 42))
                pytch.create_clone_of(self)
