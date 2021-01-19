import pytch
import math


# The world-space y-coordinate of the top of the viewport.
y_view_centre = 300


class DepthControl(pytch.Sprite):
    Costumes = []

    @pytch.when_green_flag_clicked
    def set_up_world(self):
        pytch.broadcast_and_wait("go-background")
        pytch.broadcast_and_wait("go-tanks")
        pytch.broadcast_and_wait("go-heli-shadow")
        pytch.broadcast_and_wait("go-bombs")
        pytch.broadcast_and_wait("go-heli")
        pytch.broadcast_and_wait("enable-bombing")


class Background(pytch.Sprite):
    Costumes = [("background.png", 0, 0)]
    start_shown = False

    @pytch.when_I_receive("go-background")
    def launch_clones(self):
        self.y_centre_world = 1120
        pytch.create_clone_of(self)
        self.y_centre_world = 2240
        pytch.create_clone_of(self)
        pytch.broadcast("infinite-scroll")

    @pytch.when_I_start_as_a_clone
    def set_layer_and_show(self):
        self.move_to_front_layer()
        self.show()

    @pytch.when_I_receive("infinite-scroll")
    def go_to_position(self):
        while True:
            self.go_to_xy(-240, self.y_centre_world - y_view_centre)


class ScrollControl(pytch.Sprite):
    Costumes = []

    @pytch.when_I_receive("infinite-scroll")
    def scroll_up_world(self):
        global y_view_centre
        while True:
            y_view_centre += 1
            if y_view_centre == 300 + 1120:
                y_view_centre = 300


class Helicopter(pytch.Sprite):
    Costumes = ["heli1.png", "heli2.png"]

    @pytch.when_I_receive("go-heli")
    def init(self):
        self.move_to_front_layer()
        pytch.broadcast("move-animate-heli")

    @pytch.when_I_receive("move-animate-heli")
    def rotate_blades(self):
        frame = 1
        while True:
            self.switch_costume(f"heli{int(frame)}")
            frame += 0.25
            if frame == 3:
                frame = 1

    @pytch.when_I_receive("move-animate-heli")
    def player_control(self):
        while True:
            if pytch.key_is_pressed("ArrowUp") and self.get_y() < 160:
                self.change_y(4)
            if pytch.key_is_pressed("ArrowDown") and self.get_y() > -160:
                self.change_y(-4)
            if pytch.key_is_pressed("ArrowRight") and self.get_x() < 220:
                self.change_x(4)
            if pytch.key_is_pressed("ArrowLeft") and self.get_x() > -220:
                self.change_x(-4)


class HelicopterShadow(pytch.Sprite):
    Costumes = ["helishadow1.png", "helishadow2.png"]
    start_shown = False

    @pytch.when_I_receive("go-heli-shadow")
    def init(self):
        self.move_to_front_layer()
        pytch.broadcast("move-animate-shadow")

    @pytch.when_I_receive("go-heli")
    def appear_with_heli(self):
        self.show()

    @pytch.when_I_receive("move-animate-shadow")
    def rotate_blades(self):
        frame = 1
        while True:
            self.switch_costume(f"helishadow{int(frame)}")
            frame += 0.25
            if frame == 3:
                frame = 1

    @pytch.when_I_receive("move-animate-shadow")
    def follow_helicopter(self):
        heli = Helicopter.the_original()
        while True:
            self.go_to_xy(heli.get_x() + 20, heli.get_y() - 20)


class Tank(pytch.Sprite):
    Costumes = [
        "tank0.png",
        "tank1.png",
        "tank2.png",
        "tank3.png",
        "tank4.png",
        "tank5.png",
        "tank6.png",
        "tank7.png",
        "tank8.png",
        "tank9.png",
        "tank10.png",
    ]
    start_shown = False

    @pytch.when_I_receive("go-tanks")
    def launch_clones(self):
        all_locations = [
            (100, 580),
            (-100, 580),
            (-5, 1200),
        ]
        for clone_location in all_locations:
            self.location = clone_location
            pytch.create_clone_of(self)

    @pytch.when_I_start_as_a_clone
    def keep_in_right_place(self):
        world_x, world_y = self.location
        self.move_to_front_layer()
        self.show()
        while True:
            self.go_to_xy(world_x, world_y - y_view_centre)

    def animate_explosion(self):
        for i in range(10):
            self.next_costume()
            pytch.wait_seconds(1/6)
        self.hide()
        pytch.wait_seconds(3)
        self.switch_costume("tank0")
        self.show()

    @pytch.when_I_receive("check-tank-hit")
    def check_whether_hit_by_bomb(self):
        bombs = Bomb.all_clones()
        tank_x = self.get_x()
        tank_y = self.get_y()
        with pytch.LoopIterationsPerFrame(len(bombs)):
            for bomb in bombs:
                # TODO: "distance_to()" method.
                dx = bomb.get_x() - tank_x
                dy = bomb.get_y() - tank_y
                distance = math.hypot(dx, dy)
                if distance < 30:
                    self.animate_explosion()
                    return


class BombClusterControl(pytch.Sprite):
    Costumes = []

    @pytch.when_green_flag_clicked
    def init(self):
        # Pretend an animation is in progress, so we don't allow one
        # to start until told that everything else is ready.
        self.in_progress = True

    @pytch.when_I_receive("enable-bombing")
    def enable_bombing(self):
        self.in_progress = False

    @pytch.when_key_pressed(" ")
    def maybe_launch(self):
        if self.in_progress:
            return
        self.in_progress = True
        pytch.broadcast_and_wait("drop-cluster")
        pytch.broadcast("check-tank-hit")
        pytch.broadcast_and_wait("detonate")
        self.in_progress = False


class Bomb(pytch.Sprite):
    Costumes = [
        "bomb1.png",
        "bomb2.png",
        "bomb3.png",
        "bomb4.png",
        "bomb5.png",
        "bomb6.png",
        "bomb7.png",
        "bomb8.png",
        "bomb9.png",
        "bomb10.png",
    ]

    start_shown = False

    cluster_offsets = [
        # Inner six:
        (0.5, 0.0), (0.25, 0.433), (-0.25, 0.433),
        (-0.5, 0.0), (-0.25, -0.433), (0.25, -0.433),
        # Outer twelve:
        (1.0, 0.0), (0.866, 0.5), (0.5, 0.866),
        (0.0, 1.0), (-0.5, 0.866), (-0.866, 0.5),
        (-1.0, 0.0), (-0.866, -0.5), (-0.5, -0.866),
        (0.0, -1.0), (0.5, -0.866), (0.866, -0.5),
    ]

    @pytch.when_I_receive("go-bombs")
    def init(self):
        self.move_to_front_layer()

        for offset in self.cluster_offsets:
            self.x_offset = offset[0] * 120.0
            self.y_offset = offset[1] * 120.0
            pytch.create_clone_of(self)

        self.x_offset = 0.0
        self.y_offset = 0.0

    @pytch.when_I_receive("drop-cluster")
    def drop_cluster(self):
        heli = Helicopter.the_original()
        self.go_to_xy(heli.get_x(), heli.get_y())

        self.switch_costume("bomb1")
        self.show()

        self.glide_to_xy(self.get_x() + self.x_offset,
                         self.get_y() + self.y_offset,
                         0.5)

    @pytch.when_I_receive("detonate")
    def detonate(self):
        for i in range(9):
            self.next_costume()
            pytch.wait_seconds(1/10)

        self.hide()
