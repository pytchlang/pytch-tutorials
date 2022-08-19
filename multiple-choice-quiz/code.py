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

        question_info = all_questions_info[0]

        question = question_info[0]
        ans_A = question_info[1]
        ans_B = question_info[2]
        ans_C = question_info[3]

        text = question + "\n" + ans_A + "\n" + ans_B + "\n" + ans_C
        self.say(text)
