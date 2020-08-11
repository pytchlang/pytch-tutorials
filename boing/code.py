import pytch


class BoingBackground(pytch.Stage):
    Backdrops = [
        ('boing', 'images/table.png'),
    ]


class PlayerBat(pytch.Sprite):
    Costumes = [
        ('normal', 'images/bat00.png', 60, 60),
    ]
