import pytch
from pytch import (
    Stage,
    Sprite,
    Project,
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


project = Project()
project.register_stage_class(BoingBackground)
project.go_live()
