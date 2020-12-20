import pytch


class Background(pytch.Sprite):
    Costumes = [("background.png", 0, 0)]
    start_shown = False

    @pytch.when_green_flag_clicked
    def launch_clones(self):
        self.y_start = 240
        pytch.create_clone_of(self)
        self.y_start = 240 + 1120
        pytch.create_clone_of(self)
        pytch.broadcast("infinite-scroll")

    @pytch.when_I_receive("infinite-scroll")
    def scroll(self):
        self.show()
        while True:
            self.go_to_xy(-240, self.y_start)
            self.y_start -= 1
            if self.y_start == 240 - 1120:
                self.y_start = 240 + 1120
