import pytch
import random


class Sky(pytch.Stage):
    Backdrops = ["clouds.jpg"]


class Bird(pytch.Sprite):
    Costumes = ["bird.png"]
    Sounds = ["honk.wav"]

    start_shown = False
    speed = 3

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(0, 0)
        self.set_size(0.3)
        self.show()

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        self.change_x(self.speed)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        self.change_x(-self.speed)

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):
        self.change_y(self.speed)

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        self.change_y(-self.speed)

    @pytch.when_green_flag_clicked
    def check_catch(self):
        while True:
            if self.touching(Star):
                self.say_for_seconds("Got you!", 2)


class Star(pytch.Sprite):
    Costumes = ["star.png"]

    start_shown = False

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-100, 100)
        self.set_size(0.4)
        while True:
            self.show()
            destination_x = random.randint(-240, 240)
            destination_y = random.randint(-180, 180)
            self.glide_to_xy(destination_x, destination_y, 2)

    @pytch.when_green_flag_clicked
    def check_caught(self):
        while True:
            if self.touching(Bird):
                self.hide()
