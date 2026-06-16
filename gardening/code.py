import pytch
import random

class Stage(pytch.Stage):
    Backdrops = [
        'garden.png',
        'tall_garden.png',
    ]

    @pytch.when_green_flag_clicked
    def set_global_variables(self):
        Stage.current_column = 0

        Stage.MAX_COLUMN = 3
        Stage.MIN_COLUMN = -3

        Stage.apples = 0
        self.show_variable("apples")

        Stage.water_level = 3
        self.show_variable("water_level", right=236)



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
        Stage.tree_location = 0

        for flower_patch_location in Stage.flower_patch_locations:
            soil_xpos = flower_patch_location * 48

            self.go_to_xy(soil_xpos, 0)

            if flower_patch_location == Stage.tree_location:
                # spawn grown tree
                self.switch_costume("tree_with_fruits.png")
            else:
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

    @pytch.when_I_receive("water_soil")
    def water_soil(self):
        if self.touching(Hover):
            if self.costume_name == "rose_seed.png" or self.costume_name == "daisy_seed.png":
                self.next_costume()
                self.wait_seconds(2)
                self.next_costume()
                self.wait_seconds(2)
                self.next_costume()
            elif self.costume_name == "tree_seedling.png":
                self.next_costume()
                self.wait_seconds(3)
                self.next_costume()
                self.wait_seconds(3)
                self.next_costume()



    @pytch.when_key_pressed(" ")
    def shake_down_apples(self):
        if self.costume_name == "tree_with_fruits.png" and self.touching(Hover):
            Stage.apples += 1
            self.switch_costume("tree.png")
            self.wait_seconds(3)
            self.switch_costume("tree_with_fruits.png")

    @pytch.when_key_pressed("p")
    def plant_tree(self):
        if Stage.apples > 0 and self.touching(Hover):
            Stage.apples -= 1
            self.switch_costume("tree_seedling.png")


class Water(pytch.Sprite):
    Costumes = [
        'water.png',
        'water_empty.png'
    ]

    @pytch.when_green_flag_clicked
    def spawn_water(self):
        Stage.water_locations = [-3, 3]

        for water_location in Stage.water_locations:
            water_xpos = water_location * 48

            self.go_to_xy(water_xpos, 0)
            self.create_clone()

        self.hide()

    @pytch.when_I_receive("get_water")
    def get_water(self):
        if self.costume_name == "water.png" and self.touching(Hover):
            Stage.water_level = 3

            self.next_costume()
            self.wait_seconds(10)
            self.next_costume()

class Player(pytch.Sprite):
    Costumes = [
        'player_front.png',
        'player_back.png',
        'player_left.png',
        'player_right.png',
        'player_happy.png',
        'player_sideways_left.png',
        'player_sideways_right.png',
    ]

    @pytch.when_green_flag_clicked
    def spawn_player(self):
        self.set_size(0.075)
        self.set_y(-8)

    @pytch.when_I_receive("move")
    def move(self):
        new_x = Stage.current_column * 48


class Hover(pytch.Sprite):
    Costumes = [
        'hover.png'
    ]

    @pytch.when_I_receive("move")
    def move(self):
        self.go_to_xy(Stage.current_column * 48, 0)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):

        if Stage.current_column > Stage.MIN_COLUMN:
            Stage.current_column -= 1
            self.broadcast("move")

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):

        if Stage.current_column < Stage.MAX_COLUMN:
            Stage.current_column += 1
            self.broadcast("move")

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        if Stage.current_column in Stage.water_locations:
            self.broadcast("get_water")

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):

        if Stage.water_level > 0 and Stage.current_column in Stage.flower_patch_locations:
            Stage.water_level -= 1
            self.broadcast("water_soil")
