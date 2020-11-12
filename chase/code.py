import pytch
import random

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

    @pytch.when_key_pressed('ArrowLeft')
    def move_left(self):
        self.change_x( -self.speed )

    @pytch.when_key_pressed('ArrowUp')
    def move_up(self):
        self.change_y( +self.speed )

    @pytch.when_key_pressed('ArrowDown')
    def move_down(self):
        self.change_y( -self.speed )


class Star(pytch.Sprite):
    Costumes = ['Star.png']

    start_shown = False

    @pytch.when_green_flag_clicked
    def play(self):
        self.set_size(0.4)
        self.go_to_xy(-100,100)
        while True:
            self.show()
            destination_x = random.randint(-320+66,320-66)
            destination_y = random.randint(-240+51,240-51)
            self.glide_to( destination_x, destination_y, 2 )
