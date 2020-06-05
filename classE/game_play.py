import sys
from random import randint
from os import system, name
from questions import Questions
from time import sleep
import locale


class GamePlay:
    default_answers_lst = ["A", "B", "C", "D"]
    game_info = Questions()
    total_questions_count = game_info.get_questions_count()
    question_number = 0
    help_remove_wrong_answers = 1
    help_audience = 1

    @staticmethod
    def clear_console():
        # for windows
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    @classmethod
    def asked_help(cls, player_answer):
        return player_answer == "HELP"

    @classmethod
    def answer_after_help(cls):
        possible_answers = cls.calling_help()
        player_answer = ""
        while not GamePlay.answer_from_list(player_answer, possible_answers):
            player_answer = str.upper(input("Please enter letter of the answer: "))
        return player_answer

    @classmethod
    def choose_help(cls):
        text = "Possible helps:\n"
        possible_answers = []
        player_answer = ""
        if cls.help_remove_wrong_answers == 1:
            possible_answers.append("Two answers")
            text += "Two answers - Remove two wrong answers \n"
        if cls.help_audience == 1:
            possible_answers.append("Audience")
            text += "Audience - audience guesses \n"
        print(text)
        while not GamePlay.answer_from_list(player_answer, possible_answers):
            player_answer = input(
                "Please enter help name from list - " + str(possible_answers) + ": "
            )
        if player_answer == "Audience":
            cls.audience_help(cls.question_number)
            possible_answers = cls.default_answers_lst
            cls.help_audience = 0
        else:
            possible_answers = cls.two_answers_help(cls.question_number)
            cls.help_remove_wrong_answers = 0
        return possible_answers

    @classmethod
    def calling_help(cls):
        have_helps = cls.help_remove_wrong_answers == 1 or cls.help_audience == 1
        possible_answers = cls.default_answers_lst
        if have_helps:
            possible_answers = cls.choose_help()
        else:
            print("Sorry You already used all your helps")
        return possible_answers

    @classmethod
    def player_answer_to_key(cls, txt):
        key = -1
        if txt == "A":
            return 0
        elif txt == "B":
            return 1
        elif txt == "C":
            return 2
        elif txt == "D":
            return 3
        return key

    @classmethod
    def answer_from_list(cls, answer, lst=default_answers_lst):
        result = False
        for anw in lst:
            if anw == answer:
                result = True
                break
        return result

    @classmethod
    def reset_game_parameters(cls):
        cls.question_number = 0
        cls.help_remove_wrong_answers = 1
        cls.help_audience = 1

    @classmethod
    def is_play_again(cls, answer):
        return True if answer == "Y" else False

    @classmethod
    def is_game_over(cls, quest_no, answer):
        return (
            True
            if GamePlay.game_info.get_question_correct_answer(quest_no) != answer
            else False
        )

    @staticmethod
    def end_or_restart_game():
        input_str = ""
        while input_str != "N" and input_str != "Y":
            input_str = str.upper(
                input(
                    "Do You want play again (Y/N)? Please enter letter of the answer: "
                )
            )
        if GamePlay.is_play_again(input_str):
            GamePlay.reset_game_parameters()
            GamePlay.game_play()
        else:
            sys.exit()

    @classmethod
    def two_answers_help(cls, quest_no):
        correct_answer_id = cls.game_info.get_question_correct_answer(quest_no)
        incorrect_answer_id = correct_answer_id
        all_answers = cls.game_info.get_question_answers(quest_no)
        answers = []
        while correct_answer_id == incorrect_answer_id:
            incorrect_answer_id = randint(0, len(all_answers) - 1)
        answers_id_lst = sorted([correct_answer_id, incorrect_answer_id])
        for id in answers_id_lst:
            answers.append(cls.default_answers_lst[id])
            print(all_answers[id])
        return answers

    @classmethod
    def audience_help(cls, quest_no):
        correct_answer_no = cls.game_info.get_question_correct_answer(quest_no)
        answers = cls.game_info.get_question_answers(quest_no)
        total_precent = 0
        for i in range(len(answers)):
            if i != correct_answer_no:
                precent = randint(12, 25)
                answers[i] += " " + str(precent) + "%"
                total_precent += precent
        answers[correct_answer_no] += " " + str(100 - total_precent) + "%"
        for answer in answers:
            print(answer)

    @staticmethod
    def game_play():
        GamePlay.total_questions_count -= 1
        locale.setlocale(locale.LC_ALL, "lt_LT")
        while GamePlay.question_number <= GamePlay.total_questions_count:
            GamePlay.clear_console()
            prize = GamePlay.game_info.get_prize(GamePlay.question_number)
            player_answer = ""

            if GamePlay.question_number == 0:
                print(
                    "Hello! Your first question for "
                    + locale.currency(
                        GamePlay.game_info.get_question_prizes(
                            GamePlay.question_number
                        ),
                        True,
                    )
                    + " is:\n"
                    + GamePlay.game_info.get_question(GamePlay.question_number)
                )
            else:
                print(
                    "The question for: "
                    + locale.currency(
                        GamePlay.game_info.get_question_prizes(
                            GamePlay.question_number
                        ),
                        True,
                    )
                )
                print(GamePlay.game_info.get_question(GamePlay.question_number))
            for i in GamePlay.game_info.answers[GamePlay.question_number]:
                print(i)
            while not GamePlay.answer_from_list(
                player_answer, ["A", "B", "C", "D", "HELP"]
            ):
                player_answer = str.upper(
                    input("Please enter letter of the answer or word 'HELP': ")
                )
            if True is GamePlay.asked_help(player_answer):
                player_answer = GamePlay.answer_after_help()
            if GamePlay.is_game_over(
                GamePlay.question_number, GamePlay.player_answer_to_key(player_answer)
            ):
                print("Oh noo answer is incorrect.. Game over!")
                GamePlay.end_or_restart_game()
            elif GamePlay.question_number == GamePlay.total_questions_count:
                print("Game over. Congratulations You became a millionaire")
                GamePlay.end_or_restart_game()
            else:
                print(
                    "Congratulations Your answer is correct! You already have: "
                    + locale.currency(prize, True)
                )
                sleep(0.5)
            GamePlay.question_number += 1


GamePlay.game_play()
