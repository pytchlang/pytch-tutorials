import pytch
from pytch import (
    Project,
    Stage,
    Sprite,
    when_key_pressed,
    when_green_flag_clicked,
    create_clone_of,
    when_I_start_as_a_clone,
)

import random

class BunnyStage(Stage):
  Backdrops = [ ('world', 'images/bunner-background.png') ]

  def __init__(self):
      Stage.__init__(self)
      self.switch_backdrop('world')

class Bunny(Sprite):
    Costumes = [
        ('up', 'images/sit0.png', 30, 30),
        ('right', 'images/sit1.png', 30, 30),
        ('down', 'images/sit2.png', 30, 30),
        ('left', 'images/sit3.png', 30, 30)
        ]

    def __init__(self):
        Sprite.__init__(self)
        self.switch_costume('up')
        self.go_to_xy(0, -160)
        self.show()

    @when_key_pressed('ArrowUp')
    def move_up(self):
        self.switch_costume('up')
        if self.get_y() < 150:
            self.change_y(40)

    @when_key_pressed('ArrowRight')
    def move_right(self):
        self.switch_costume('right')
        if self.get_x() < 210:
            self.change_x(25)

    @when_key_pressed('ArrowDown')
    def move_down(self):
        self.switch_costume('down')
        if self.get_y() > -150:
            self.change_y(-40)

    @when_key_pressed('ArrowLeft')
    def move_left(self):
        self.switch_costume('left')
        if self.get_x() > -210:
            self.change_x(-25)

class Car(Sprite):
    Costumes = [
        ('left0', 'images/car00.png', 45, 30),
        ('right0', 'images/car01.png', 45, 30),
        ('left1', 'images/car20.png', 45, 30),
        ('right1', 'images/car21.png', 45, 30)
        ]

    def __init__(self):
        Sprite.__init__(self)
        self.speed = 3
        self.direction = 'nothing'
        self.set_size(0.65)
        self.hide()

    @when_green_flag_clicked
    def startTrafficRowOne(self):
        while True:
            if random.random() < 0.2:
                self.go_to_xy(-285,-125)
                self.direction = 'right'
                create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @when_green_flag_clicked
    def startTrafficRowTwo(self):
        while True:
            if random.random() < 0.2:
                self.go_to_xy(285,-80)
                self.direction = 'left'
                create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @when_green_flag_clicked
    def startTrafficRowThree(self):
        while True:
            if random.random() < 0.2:
                self.go_to_xy(-285,-30)
                self.direction = 'right'
                create_clone_of(self)
                pytch.wait_seconds(0.3)
            pytch.wait_seconds(0.1)

    @when_I_start_as_a_clone
    def drive(self):
        self.switch_costume( self.direction + random.choice(['0','1']) )
        self.show()
        if self.direction == 'right':
            while self.get_x() < 285:
                self.change_x( self.speed )
        else: # Direction should be 'left'
            while self.get_x() > -285:
                self.change_x( -self.speed )
        self.hide()
        self.delete_this_clone()

    @when_I_start_as_a_clone
    def check_for_collision(self):
        while True:
            while not self.touching(Bunny):
                pass
            print "Squish the bunny!"

