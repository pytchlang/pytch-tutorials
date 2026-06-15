import pytch
import random

class Stage(pytch.Stage):
    Backdrops = [
        'garden.png',
        'tall_garden.png',
    ]

    @pytch.when_green_flag_clicked
    def set_global_variable(self):
        Stage.current_column = 0

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
            soil_xpos = flower_patch_location * 48

            self.go_to_xy(soil_xpos, 0)

            rng = random.randint(0, 4)
            if rng < 1:
                # pick rose seed (25% chance)
                self.switch_costume("rose_seed.png")
            elif rng < 2:
                # pick daisy seed (25% chance)
                self.switch_costume("daisy_seed.png")
            else:
                # pick nothing
                self.switch_costume("empty.png")

            self.create_clone()

        self.hide()

class Hover(pytch.Sprite):
    Costumes = [
        'hover.png'
    ]

    @pytch.when_I_receive("move")
    def move(self):
        self.go_to_xy(Stage.current_column * 48, 0)

