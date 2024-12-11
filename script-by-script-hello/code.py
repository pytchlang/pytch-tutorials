import pytch
import random

class Snake(pytch.Sprite):
    Costumes = ["Pytch-hello-snake.png"]

    @pytch.when_this_sprite_clicked
    def speak(self):
        pass
