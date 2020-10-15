import pytch


class Background(pytch.Stage):
    Backdrops = ["background.png"]


class Block(pytch.Sprite):
    Costumes = ["block-unlit.png", "block-lit.png"]

    @pytch.when_green_flag_clicked
    def create_pyramid(self):
        for r in range(7):
            for b in range(7 - r):
                block_x = -150 + (b * 56) + (r * 28)
                block_y = -145 + (r * 42)
                self.go_to_xy(block_x, block_y)
                pytch.create_clone_of(self)
        self.hide()


class Qbert(pytch.Sprite):
    Costumes = ["qbert0.png", "qbert1.png", "qbert2.png", "qbert3.png"]
