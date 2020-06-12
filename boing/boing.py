import pytch
from pytch import (
    Stage,
    Project,
)


class BoingBackground(Stage):
    Backdrops = [('boing', 'images/table.png')]

    def __init__(self):
        Stage.__init__(self)
        self.switch_backdrop('boing')


project = Project()
project.register_stage_class(BoingBackground)
project.go_live()
