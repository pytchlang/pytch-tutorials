import pytch
from pytch import (
    Stage,
    Sprite,
    Project,
    when_green_flag_clicked,
)


class BoingBackground(Stage):
    Backdrops = [('boing', 'images/table.png')]

    def __init__(self):
        Stage.__init__(self)
        self.switch_backdrop('boing')


class Bat(Sprite):
    Costumes = [('normal', 'images/bat00.png', 60, 60)]

    def __init__(self):
        Sprite.__init__(self)
        self.switch_costume('normal')

    @when_green_flag_clicked
    def get_ready_to_play(self):
        self.go_to_xy(-215, 0)
        self.show()


project = Project()
project.register_stage_class(BoingBackground)
project.register_sprite_class(Bat)
project.go_live()
