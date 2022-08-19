import pytch


all_questions_info = [
    [
        "What is the capital of Ireland?",
        "Dublin",
        "Cork",
        "Galway",
        "A",
    ],
    [
        "How many centimetres are there in one metre?",
        "10",
        "100",
        "1000",
        "B",
    ],
    [
        "What year was the Anglo-Irish Treaty signed?",
        "1921",
        "1922",
        "1923",
        "A",
    ],
]

n_questions = len(all_questions_info)

clicked = False
answer = None


class Narrator(pytch.Sprite):
    Costumes = ["button-question.png"]

    @pytch.when_green_flag_clicked
    def play_quiz(self):
        global clicked

        self.say_for_seconds("Let's begin!", 3)

        score = 0
        question_index = 0

        while question_index < n_questions:

            question_info = all_questions_info[question_index]

            question = question_info[0]
            ans_A = "A: " + question_info[1]
            ans_B = "B: " + question_info[2]
            ans_C = "C: " + question_info[3]

            text = question + "\n" + ans_A + "\n" + ans_B + "\n" + ans_C
            self.say(text)

            clicked = False
            while not clicked:
                pass

            correct_answer = question_info[4]
            if answer == correct_answer:
                self.say_for_seconds("Correct!", 2)
            else:
                self.say_for_seconds("Sorry, that's not correct.", 2)

            question_index += 1


class AnswerA(pytch.Sprite):
    Costumes = ["button-ans-A.png"]

    @pytch.when_green_flag_clicked
    def setup(self):
        self.go_to_xy(-140, -120)

    @pytch.when_this_sprite_clicked
    def notify_answered(self):
        global clicked, answer
        answer = "A"
        clicked = True


class AnswerB(pytch.Sprite):
    Costumes = ["button-ans-B.png"]

    @pytch.when_green_flag_clicked
    def setup(self):
        self.go_to_xy(0, -120)

    @pytch.when_this_sprite_clicked
    def notify_answered(self):
        global clicked, answer
        answer = "B"
        clicked = True


class AnswerC(pytch.Sprite):
    Costumes = ["button-ans-C.png"]

    @pytch.when_green_flag_clicked
    def setup(self):
        self.go_to_xy(140, -120)

    @pytch.when_this_sprite_clicked
    def notify_answered(self):
        global clicked, answer
        answer = "C"
        clicked = True
