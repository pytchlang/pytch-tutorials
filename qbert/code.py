import pytch


class Background(pytch.Stage):
    Backdrops = ["background.png"]


class Block(pytch.Sprite):
    Costumes = ["block0.png", "block1.png"]
    start_shown = False

    @pytch.when_green_flag_clicked
    def create_pyramid(self):
        for r in range(7):
            for b in range(7 - r):
                block_x = -150 + (b * 56) + (r * 28)
                block_y = -145 + (r * 42)
                self.go_to_xy(block_x, block_y)
                pytch.create_clone_of(self)
        pytch.broadcast("set-up-qbert")

    @pytch.when_I_start_as_a_clone
    def appear(self):
        self.set_size(0.875)
        self.show()


class Qbert(pytch.Sprite):
    Costumes = ["qbert0.png", "qbert1.png", "qbert2.png", "qbert3.png"]
    start_shown = False

    # This list must have exactly 14 entries.
    bounce = [6, 4, 2, 1, 0, 0, 0, 0, 0, 0, -1, -2, -4, -6]

    @pytch.when_I_receive("set-up-qbert")
    def go_to_starting_position(self):
        self.go_to_xy(-150 + 3 * 56, -145 + (6 * 42) + 28)
        self.switch_costume("qbert1")
        self.go_to_front_layer()
        self.show()
        self.jumping = False

    def pyramid_coordinates(self):
        y_on_stage = self.y_position
        pyramid_r = (y_on_stage + 145 - 28) / 42
        x_on_stage = self.x_position
        pyramid_b = (x_on_stage + 150 - pyramid_r * 28) / 56
        return (pyramid_r, pyramid_b)

    def jump(self, x_speed, y_speed, costume):
        if self.jumping:
            return
        self.jumping = True
        self.switch_costume(costume)
        for frame in range(14):
            self.change_x(x_speed)
            self.change_y(y_speed + self.bounce[frame])

        r, b = self.pyramid_coordinates()
        if r < 0 or r >= 7 or b < 0 or b >= (7 - r):
            pytch.broadcast("fall-off")

        self.jumping = False

    @pytch.when_I_receive("fall-off")
    def disappear(self):
        for i in range(100, 10, -5):
            self.set_size(i / 100.0)
        self.hide()

    @pytch.when_key_pressed("ArrowUp")
    def jump_up(self):
        self.jump(2, 3, "qbert0")

    @pytch.when_key_pressed("ArrowDown")
    def jump_down(self):
        self.jump(-2, -3, "qbert2")

    @pytch.when_key_pressed("ArrowLeft")
    def jump_left(self):
        self.jump(-2, 3, "qbert3")

    @pytch.when_key_pressed("ArrowRight")
    def jump_right(self):
        self.jump(2, -3, "qbert1")