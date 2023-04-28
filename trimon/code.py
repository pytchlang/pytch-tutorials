import pytch

pattern = [1, 2, 3, 1]


class Background(pytch.Stage):
    Backdrops = ["blue-gradient.png"]

    @pytch.when_key_pressed("p")
    def play_pattern(self):
        for led in pattern:
            message = "flash-" + str(led)
            pytch.broadcast_and_wait(message)


class LED1(pytch.Sprite):
    Costumes = ["light-off.png", "light-on.png"]
    Sounds = ["note-1.mp3"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(-140, 80)

    @pytch.when_I_receive("flash-1")
    def flash(self):
        self.switch_costume(1)
        self.play_sound_until_done("note-1")
        self.switch_costume(0)


class LED2(pytch.Sprite):
    Costumes = ["light-off.png", "light-on.png"]
    Sounds = ["note-2.mp3"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(0, 80)


class LED3(pytch.Sprite):
    Costumes = ["light-off.png", "light-on.png"]
    Sounds = ["note-3.mp3"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(140, 80)
