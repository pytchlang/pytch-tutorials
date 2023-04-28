import pytch

pattern = [1, 2, 3, 1]
user_attempt = []
light_flashing = False


class Background(pytch.Stage):
    Backdrops = ["blue-gradient.png"]

    @pytch.when_key_pressed("p")
    def play_pattern(self):
        for led in pattern:
            message = "flash-" + str(led)
            pytch.broadcast_and_wait(message)
            pytch.wait_seconds(0.1)

    @pytch.when_I_receive("check-user-attempt")
    def check_user_attempt(self):
        user_attempt_length = len(user_attempt)
        pattern_start = pattern[:user_attempt_length]


class LED1(pytch.Sprite):
    Costumes = ["light-off.png", "light-on.png"]
    Sounds = ["note-1.mp3"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(-140, 80)

    @pytch.when_I_receive("flash-1")
    def flash(self):
        self.switch_costume(1)
        self.play_sound_until_done("note-1")
        self.switch_costume(0)


class Button1(pytch.Sprite):
    Costumes = ["green-button.png"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(-140, -80)

    @pytch.when_this_sprite_clicked
    def press_button(self):
        global light_flashing, user_attempt
        if light_flashing:
            return
        light_flashing = True
        pytch.broadcast_and_wait("flash-1")
        user_attempt.append(1)
        light_flashing = False


class LED2(pytch.Sprite):
    Costumes = ["light-off.png", "light-on.png"]
    Sounds = ["note-2.mp3"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(0, 80)

    @pytch.when_I_receive("flash-2")
    def flash(self):
        self.switch_costume(1)
        self.play_sound_until_done("note-2")
        self.switch_costume(0)


class Button2(pytch.Sprite):
    Costumes = ["green-button.png"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(0, -80)

    @pytch.when_this_sprite_clicked
    def press_button(self):
        global light_flashing, user_attempt
        if light_flashing:
            return
        light_flashing = True
        pytch.broadcast_and_wait("flash-2")
        user_attempt.append(2)
        light_flashing = False


class LED3(pytch.Sprite):
    Costumes = ["light-off.png", "light-on.png"]
    Sounds = ["note-3.mp3"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(140, 80)

    @pytch.when_I_receive("flash-3")
    def flash(self):
        self.switch_costume(1)
        self.play_sound_until_done("note-3")
        self.switch_costume(0)


class Button3(pytch.Sprite):
    Costumes = ["green-button.png"]

    @pytch.when_green_flag_clicked
    def move_to_position(self):
        self.go_to_xy(140, -80)

    @pytch.when_this_sprite_clicked
    def press_button(self):
        global light_flashing, user_attempt
        if light_flashing:
            return
        light_flashing = True
        pytch.broadcast_and_wait("flash-3")
        user_attempt.append(3)
        light_flashing = False
