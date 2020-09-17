import pytch

class Bird(pytch.Sprite):
    Costumes = [('bird', 'images/game-1582150_1280.png', 166, 108)]

    @when_green_flag_clicked
    def start(self):
        self.show()
        self.set_size(0.3)
        self.go_to_xy(0,0)

    @when_key_pressed('ArrowRight')
    def move_right(self):
        self.change_x( 5 )

    @when_key_pressed('ArrowLeft')
    def move_left(self):
        self.change_x( -5 )

    @when_key_pressed('ArrowUp')
    def move_up(self):
        self.change_y( +5 )

    @when_key_pressed('ArrowDown')
    def move_down(self):
        self.change_y( -5 )
