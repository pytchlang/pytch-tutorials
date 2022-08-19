import pytch


all_questions_info = [
    [
        "What is the capital of Ireland?",
        "Dublin",
        "Cork",
        "Galway",
        "A",
    ],
]


class Narrator(pytch.Sprite):
    Costumes = ["button-question.png"]

    @pytch.when_green_flag_clicked
    def play_quiz(self):
        self.say_for_seconds("Let's begin!", 3)
