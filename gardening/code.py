import pytch
import random

class Stage(pytch.Stage):
    Backdrops = [
        'garden.png',
        'tall_garden.png',
    ]


class Soil(pytch.Sprite):
    Costumes = [
        'tree_seedling.png',
        'tree_small.png',
        'tree.png',
        'tree_with_fruits.png',
        'rose_seed.png',
        'rose_1.png',
        'rose_2.png',
        'rose.png',
        'daisy_seed.png',
        'daisy_1.png',
        'daisy_2.png',
        'daisy.png',
        'empty.png',
    ]

    @pytch.when_green_flag_clicked
    def spawn_soil(self):
        Stage.flower_patch_locations = [-2, -1, 0, 1, 2]

        for flower_patch_location in Stage.flower_patch_locations:
            self.create_clone()
