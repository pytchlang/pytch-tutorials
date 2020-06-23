import pytch
from pytch import (
    Project,
    Stage,
)

class BunnyStage(Stage):
  Backdrops = [ ('world', 'images/bunner-background.png') ]

  def __init__(self):
      Stage.__init__(self)
      self.switch_backdrop('world')

