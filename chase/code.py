import pytch

class Sky(pytch.Stage):
    Backdrops=["clouds.jpg"]

class Bird(pytch.Sprite):
    Costumes = ['Bird.png']

    start_shown = False
    speed = 3

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(0,0)
        self.set_size(0.3)
        self.show()

    @pytch.when_key_pressed('ArrowRight')
    def move_right(self):
        self.change_x( self.speed )