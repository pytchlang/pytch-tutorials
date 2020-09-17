import pytch

class Bird(pytch.Sprite):
    Costumes = [('bird', 'images/game-1582150_1280.png', 166, 108)]

    @when_green_flag_clicked
    def start(self):
        self.show()
        self.set_size(0.3)
