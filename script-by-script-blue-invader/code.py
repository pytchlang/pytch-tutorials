import pytch
import random


class Stage(pytch.Stage):
    Backdrops = ["galaxy.png"]

    @pytch.when_green_flag_clicked
    def run(self):
        Stage.score = 0
        pytch.show_variable(Stage, "score")
        pytch.broadcast_and_wait("make-clones")
        pytch.broadcast_and_wait("play-game")


class Alien(pytch.Sprite):
    Costumes = [
        "Invader_Navy_1.png",
        "Invader_Navy_2.png",
        "Invader_Green_1.png",
        "Invader_Green_2.png",
        "Invader_DarkRed_1.png",
        "Invader_DarkRed_2.png",
        "Invader_Blue_1.png",
        "Invader_Blue_2.png",
        "Invader_Cyan_1.png",
        "Invader_Cyan_2.png",
        "Invader_Orange_1.png",
        "Invader_Orange_2.png",
        "Invader_Pink_1.png",
        "Invader_Pink_2.png",
        "Invader_Red_1.png",
        "Invader_Red_2.png",
        "Invader_Yellow_1.png",
        "Invader_Yellow_2.png"
    ]

    @pytch.when_I_receive("make-clones")
    def make_clones(self):
        self.go_to_xy(-150, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(-90, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(-30, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(30, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(90, 180)
        pytch.create_clone_of(self)
        self.go_to_xy(150, 180)

    @pytch.when_I_receive("play-game")
    def drift_down_screen(self):
        self.set_size(0.15)
        while True:
            costume_index = random.choice([0, 2])
            self.switch_costume(costume_index)
            self.set_y(180)
            self.show()
            glide_time = random.uniform(3.0, 5.0)
            self.glide_to_xy(self.x_position, -180, glide_time)

    @pytch.when_this_sprite_clicked
    def handle_hit(self):
        self.hide()
