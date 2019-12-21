import string


def get_questions_prizes():
    return {0: 100, 1: 1000, 2: 10000, 3: 100000, 4: 1000000}


def get_questions():
    return {0: "How much is 2 + 2",
            1: "What is the capital of Lithuania",
            2: "What is the biggest animal in the World",
            3: "What is the president of Germany",
            4: "What is the longest river in Europe"}


def get_correct_answers():
    return {0: 0, 1: 1, 2: 0, 3: 2, 4: 3}


def get_answers():
    return {0: ["A. 4", "B. 16", "C. 5", "D. 7"], 1: ["A. Kaunas", "B. Vilnius", "C. Riga", "D. Warsaw"],
            2: ["A. Blue whale", "B. Hippos", "C. Giraffe", "D. Elephant"],
            3: ["A. Angela Merkel", "B. Joachim Gauck", "C. Frank-Walter Steinmeier", "D. Donald Trump"],
            4: ["A. Danube", "B. Ural", "C. Kama", "D. Volga"]}


class Questions:

    def __init__(self):
        self.questions = get_questions()
        self.correct_answers = get_correct_answers()
        self.answers = get_answers()
        self.prizes = get_questions_prizes()

    def get_question(self, question_no):
        return self.questions.get(question_no)

    def get_question_answers(self, question_no):
        return self.answers.get(question_no)

    def get_question_correct_answer(self, question_no):
        return self.correct_answers.get(question_no)

    def get_question_prizes(self, question_no):
        return self.prizes.get(question_no)

    def get_prize(self, question_no):
        return self.prizes.get(question_no)

    def get_question_data(self, question_no) -> dict:
        return {"question": self.get_question(question_no),
                "answers": self.get_question_answers(question_no),
                "prize": self.get_question_prizes(question_no),
                "correctAnswer": self.get_question_correct_answer(question_no)}

    def get_next_question_no(self):
        return (sorted(self.questions.keys())[-1]) + 1

    def create_new_question(self, question: string, answers: list, prize: int, correct_answer: string) -> int:
        next_question_no = self.get_next_question_no()
        self.questions[next_question_no] = question
        self.answers[next_question_no] = answers
        self.prizes[next_question_no] = prize
        self.correct_answers[next_question_no] = correct_answer

        return next_question_no

    def change_question(self, question_no: int, question: string, answers: list, prize: int, correct_answer: string) \
            -> string:
        answer = "The question number does not exists, go create a new question"
        if question_no in self.questions.keys():
            self.questions[question_no] = question
            self.answers[question_no] = answers
            self.prizes[question_no] = prize
            self.correct_answers[question_no] = correct_answer
            answer = "The question was changed successfully"
        return answer

    def remove_question(self, question_no: int) -> string:
        try:
            del self.questions[question_no]
            del self.answers[question_no]
            del self.prizes[question_no]
            del self.correct_answers[question_no]
        except KeyError:
            return "The question number does not exists!"
        return "The Question was removed successfully"

    def get_questions_count(self):
        return len(self.questions)
