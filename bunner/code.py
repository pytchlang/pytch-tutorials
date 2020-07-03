import pytch

import random


game_running = False

score = 0

WAITING, PLAYING, SQUISHED, DROWNING = range(4)


class BunnyStage(pytch.Stage):
    Backdrops = [("world", "bunner-background.png"),
                 ("gameover", "gameover-background.png")]

    @pytch.when_I_receive("start playing")
    def start_game(self):
        self.switch_backdrop("world")

    @pytch.when_I_receive("game over")
    def game_over(self):
        self.switch_backdrop("gameover")


class Bunny(pytch.Sprite):
    Costumes = [
        ("up", "sit0.png"),
        ("right", "sit1.png"),
        ("down", "sit2.png"),
        ("left", "sit3.png"),
        ("up_squished", "splat0.png"),
        ("right_squished", "splat1.png"),
        ("down_squished", "splat2.png"),
        ("left_squished", "splat3.png"),
    ] + [
        ("splash-%d" % n, "splash%d.png" % n) for n in range(8)
    ]

    start_shown = False

    @pytch.when_green_flag_clicked
    def go_to_starting_position(self):
        self.switch_costume("up")
        self.go_to_xy(0, -160)
        self.mode = PLAYING
        self.hide()
        self.mode = WAITING
        self.lives = -1
        self.highest_row_reached = 0
        self.current_row = 0

    @pytch.when_I_receive("start playing")
    def start_game(self):
        global game_running, score
        self.lives = 3
        score = 0
        game_running = True
        self.play_one_life()

    def play_one_life(self):
        if self.lives > 0:
            self.lives = self.lives - 1
            pytch.broadcast("lives changed")
            self.switch_costume("up")
            self.go_to_xy(0, -160)
            self.highest_row_reached = 0
            self.current_row = 0
            self.mode = PLAYING
            self.show()
        else:
            global game_running
            game_running = False
            pytch.broadcast("game over")
            self.hide()
            self.mode = WAITING

    @pytch.when_I_receive("start playing")
    def watch_for_water(self):
        while game_running:
            if (self.get_y() > 30 and self.get_y() < 160 and
                    not self.touching(Log)):
                self.mode = DROWNING

    @pytch.when_key_pressed("ArrowUp")
    def move_up(self):
        global score
        if self.mode == PLAYING:
            self.switch_costume("up")
            if self.get_y() < 150:
                self.change_y(40)
                self.current_row = self.current_row + 1
                if self.current_row > self.highest_row_reached:
                    self.highest_row_reached = self.current_row
                    score = score + 1
                    pytch.broadcast("score changed")

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        if self.mode == PLAYING:
            self.switch_costume("right")
            if self.get_x() < 210:
                self.change_x(25)

    @pytch.when_key_pressed("ArrowDown")
    def move_down(self):
        if self.mode == PLAYING:
            self.switch_costume("down")
            if self.get_y() > -150:
                self.change_y(-40)
                self.current_row = self.current_row - 1

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        if self.mode == PLAYING:
            self.switch_costume("left")
            if self.get_x() > -210:
                self.change_x(-25)

    @pytch.when_I_receive("squish bunny")
    def squish(self):
        if self.mode != SQUISHED:
            self.mode = SQUISHED
            self.switch_costume(self._appearance + "_squished")
            pytch.wait_seconds(0.5)
            self.play_one_life()


class Car(pytch.Sprite):
    Costumes = [
        ("left0", "car00.png"),
        ("right0", "car01.png"),
        ("left1", "car20.png"),
        ("right1", "car21.png"),
    ]

    start_shown = False

    @pytch.when_I_receive("start playing")
    def startTrafficRowOne(self):
        global game_running
        self.speed = 3
        while game_running:
            if random.random() < 0.2:
                self.go_to_xy(-285, -125)
                self.direction = "right"
                pytch.create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @pytch.when_I_receive("start playing")
    def startTrafficRowTwo(self):
        global game_running
        self.speed = 3
        while game_running:
            if random.random() < 0.2:
                self.go_to_xy(285, -80)
                self.direction = "left"
                pytch.create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @pytch.when_I_receive("start playing")
    def startTrafficRowThree(self):
        global game_running
        self.speed = 3
        while game_running:
            if random.random() < 0.2:
                self.go_to_xy(-285, -30)
                self.direction = "right"
                pytch.create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @pytch.when_I_start_as_a_clone
    def drive(self):
        self.switch_costume(self.direction + random.choice(["0", "1"]))
        self.set_size(0.65)
        self.show()
        if self.direction == "right":
            while self.get_x() < 285:
                self.change_x( self.speed )
        else: # Direction should be "left"
            while self.get_x() > -285:
                self.change_x( -self.speed )
        self.hide()
        self.delete_this_clone()

    @pytch.when_I_start_as_a_clone
    def check_for_collision(self):
        while True:
            while not self.hits(Bunny.the_original()):
                pass
            pytch.broadcast("squish bunny")

    @pytch.when_I_receive("game over")
    def vanish(self):
        self.delete_this_clone()

    def hits(self, other):
        return (abs(self.get_y() - other.get_y()) <= 10 and
                abs(self.get_x() - other.get_x()) <= 40)


class StartButton(pytch.Sprite):
    Costumes = ["start.png"]

    start_shown = False

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(0,120)
        self.show()

    @pytch.when_I_receive("game over")
    def game_over_try_again(self):
        pytch.wait_seconds(1)
        self.show()

    @pytch.when_this_sprite_clicked
    def start_new_game(self):
        pytch.broadcast("start playing")
        self.hide()


score_costumes = [("digit-%d" % n, "digit-%d.png" % n, 14, 14)
                  for n in range(10)]


class Score_1(pytch.Sprite):
    Costumes = score_costumes

    @pytch.when_green_flag_clicked
    def set_position_and_size(self):
        self.go_to_xy(200, 162)
        self.hide()

    @pytch.when_I_receive("score changed")
    def show_correct_digit(self):
        self.switch_costume("digit-%d" % (score % 10) )
        self.show()


class Score_2(pytch.Sprite):
    Costumes = score_costumes

    @pytch.when_green_flag_clicked
    def set_position_and_size(self):
        self.go_to_xy(175, 162)
        self.hide()

    @pytch.when_I_receive("score changed")
    def show_correct_digit(self):
        self.switch_costume("digit-%d" % (score // 10) )
        self.show()


class LivesCounter(pytch.Sprite):
    Costumes = score_costumes

    @pytch.when_green_flag_clicked
    def set_position_and_size(self):
        self.go_to_xy(20, 162)
        self.hide()

    @pytch.when_I_receive("lives changed")
    def show_correct_digit(self):
        self.switch_costume("digit-%d" % (Bunny.the_original().lives % 10))
        self.show()


class Log(pytch.Sprite):
    Costumes = ["log0.png", "log1.png"]

    start_shown = False

    @pytch.when_I_receive("start playing")
    def start_row_1(self):
        self.start_row("right", 30)

    @pytch.when_I_receive("start playing")
    def start_row_2(self):
        self.start_row("left", 80)

    @pytch.when_I_receive("start playing")
    def start_row_3(self):
        self.start_row("right", 130)

    def start_row(self, direction, y):
        self.speed = 3
        if direction == "right":
            x = -285
        else:
            x = 285

        while game_running:
            if random.random() < 0.05:
                self.go_to_xy( x, y )
                self.direction = direction
                pytch.create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @pytch.when_I_start_as_a_clone
    def start_log(self):
        self.switch_costume("log" + random.choice(["0", "1"]))
        self.set_size(0.65)
        self.show()
        if self.direction == "left":
            while( self.get_x() > -285):
                self.change_x( -self.speed )
                if self.hits( Bunny.the_original() ):
                    Bunny.the_original().change_x( -self.speed )
        else: # Right
            while( self.get_x() < 285):
                self.change_x( self.speed )
                if self.hits( Bunny.the_original() ) and Bunny.the_original().mode != DROWNING:
                    Bunny.the_original().change_x( self.speed )
        self.hide()
        self.delete_this_clone()

    @pytch.when_I_receive("game over")
    def vanish(self):
        self.delete_this_clone() # Does nothing on the non-clone original

    def hits(self, other):
        return (abs(self.get_y() - other.get_y()) <= 10 and
                abs(self.get_x() - other.get_x()) <= 40)
