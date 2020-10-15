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
                self.go_to_xy(-150 + (b * 56) + (r * 28),
                              -145 + (r * 42))
                pytch.create_clone_of(self)
        pytch.broadcast("set-up-qbert")

    @pytch.when_I_start_as_a_clone
    def appear(self):
        self.set_size(0.875)
        self.show()


class Qbert(pytch.Sprite):
    Costumes = ["qbert0.png", "qbert1.png", "qbert2.png", "qbert3.png"]
    start_shown = False

    @pytch.when_I_receive("set-up-qbert")
    def go_to_starting_position(self):
        self.go_to_xy(-150 + 3 * 56, -145 + (6 * 42) + 28)
        self.switch_costume("qbert1")
        self.move_to_front_layer()
        self.show()

    def jump(self, x_speed, y_speed, costume):
        self.switch_costume(costume)
        for frame in range(14):
            self.change_x(x_speed)
            self.change_y(y_speed)

    @pytch.when_key_pressed("ArrowUp")
    def jump_up(self):
        self.switch_costume("qbert0")
        for frame in range(14):
            self.change_x(2)
            self.change_y(3)

    @pytch.when_key_pressed("ArrowDown")
    def jump_down(self):
        self.switch_costume("qbert2")
        for frame in range(14):
            self.change_x(-2)
            self.change_y(-3)
