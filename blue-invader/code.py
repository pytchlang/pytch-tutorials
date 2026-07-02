import pytch


class Alien(pytch.Sprite):
    Costumes = ["Invader_Navy_1.png", "Invader_Green_1.png"]

    @pytch.when_green_flag_clicked
    def make_sensible_size(self):
        self.set_size(0.15)


class Galaxy(pytch.Stage):
    Backdrops = ["starry-sky.jpg"]
