import pytch


class Sky(pytch.Stage):
    Backdrops = ["clouds.jpg"]


class Bird(pytch.Sprite):
    Costumes = ["bird.png"]

    start_shown = False
