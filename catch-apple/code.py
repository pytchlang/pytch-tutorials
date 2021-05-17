import pytch


class Bowl(pytch.Sprite):
    Costumes = ["bowl.png"]

    @pytch.when_green_flag_clicked
    def move_with_keys(self):
        self.go_to_xy(0, -145)

        while True:
            if pytch.key_is_pressed("a"):
                if self.get_x() >= -145:
                    self.change_x(-2)
            if pytch.key_is_pressed("d"):
                if self.get_x() <= 190:
                    self.change_x(2)


class Apple(pytch.Sprite):
    Costumes = ["apple.png"]

    @pytch.when_green_flag_clicked
    def move_down_screen(self):
        self.go_to_xy(100, 200)
        while self.get_y() > -140:
            self.change_y(-3)
            if self.touching(Bowl):
                self.hide()
                return


class ScoreKeeper(pytch.Sprite):
    Costumes = ["Dani.png"]

    @pytch.when_green_flag_clicked
    def initialise(self):
        self.go_to_xy(-215, -115)
        self.score = 0
        self.say(self.score)

    def award_point(self):
        self.score += 1
        self.say(self.score)
