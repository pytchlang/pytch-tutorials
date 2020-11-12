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
            destination_x = random.randint(-320 + 66, 320 - 66)
            destination_y = random.randint(-240 + 51, 240 - 51)
            self.glide_to(destination_x, destination_y, 2)

    def glide_to(self, x, y, seconds):
        steps_per_sec = 25
        steps = seconds * steps_per_sec
        wait = 1.0 / steps_per_sec
        stepx = (x - self.get_x()) / float(steps)
        stepy = (y - self.get_y()) / float(steps)
        for _ in range(steps):
            self.change_x(stepx)
            self.change_y(stepy)
            pytch.wait_seconds(wait)

    @pytch.when_green_flag_clicked
    def check_caught(self):
        while True:
            if self.touching(Bird):
                self.hide()
