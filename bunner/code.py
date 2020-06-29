import pytch
from pytch import (
    Project,
    Stage,
    Sprite,
    when_key_pressed
)

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
