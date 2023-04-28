import pytch


class Background(pytch.Stage):
    Backdrops = ["blue-gradient.png"]


class LED1(pytch.Sprite):
    Costumes = ["light-off.png", "light-on.png"]
    Sounds = ["note-1.mp3"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(-140, 80)

    @pytch.when_this_sprite_clicked
    def flash(self):
        self.switch_costume(1)
        self.play_sound_until_done("note-1")
        self.switch_costume(0)
