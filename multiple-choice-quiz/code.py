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


class Narrator(pytch.Sprite):
    Costumes = ["button-question.png"]

    @pytch.when_green_flag_clicked
    def play_quiz(self):
        self.say_for_seconds("Let's begin!", 3)

        question_index = 0

        while question_index < n_questions:

            question_info = all_questions_info[question_index]

            question = question_info[0]
            ans_A = "A: " + question_info[1]
            ans_B = "B: " + question_info[2]
            ans_C = "C: " + question_info[3]

            text = question + "\n" + ans_A + "\n" + ans_B + "\n" + ans_C
            self.say(text)

            pytch.wait_seconds(2)

            question_index += 1


class AnswerA(pytch.Sprite):
    Costumes = ["button-ans-A.png"]

    @pytch.when_green_flag_clicked
    def setup(self):
        self.go_to_xy(-140, -120)
