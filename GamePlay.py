import sys
from random import randint
from subprocess import call
from Questions import Questions


class GamePlay:

    @staticmethod
    def game_play():

        game_info = Questions()
        total_questions_count = game_info.get_questions_count()
        question_number = 0
        left_help = 1

        def player_answer_to_key(txt):
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

        def answer_from_list(answer):
            result = False
            lst = ["A", "B", "C", "D"]
            for anw in lst:
                if anw == answer:
                    result = True
                    break
            return result

        def reset_game_parameters():
            nonlocal question_number
            question_number = 0
            nonlocal left_help
            left_help = 1

        def is_play_again(answer):
            return True if answer == "Y" else False

        def is_game_over(quest_no, answer):
            return True if game_info.get_question_correct_answer(quest_no) != answer else False

        def end_or_restart_game():
            input_str = ""
            while input_str != "N" and input_str != "Y":
                input_str = str.upper(input("Do You want play again (Y/N)? Please enter letter of the answer: "))
            if is_play_again(input_str):
                GamePlay.game_play()
            else:
                sys.exit()

        def print_two_answer(quest_no):
            correct_answer = game_info.get_question_answers(quest_no)[game_info.get_question_correct_answer(quest_no)]
            incorrect_answer = correct_answer
            all_answers = game_info.get_question_answers(quest_no)
            while correct_answer == incorrect_answer:
                incorrect_answer = all_answers[randint(0, len(all_answers) - 1)]
            answers = sorted([correct_answer, incorrect_answer])
            for answer in answers:
                print(answer)

        total_questions_count -= 1
        while question_number <= total_questions_count:
            prize = game_info.get_prize(question_number)
            player_answer = ""

            if question_number == 0:
                print("Hello! Your first question for " + str(game_info.get_question_prizes(question_number)) + " is: €"
                      + game_info.get_question(question_number))
            else:
                print("The question for: " + str(game_info.get_question_prizes(question_number)))
                print(game_info.get_question(question_number))

            for i in game_info.answers[question_number]:
                print(i)

            while left_help > 0 and player_answer is not ("N" or "Y"):
                player_answer = input("Do you want to remove two incorrect answers (Y/N)? ")

                if player_answer is "Y":
                    print_two_answer(question_number)
                    left_help -= 1

            while not answer_from_list(player_answer):
                player_answer = str.upper(input("Please enter letter of the answer: "))

            if is_game_over(question_number, player_answer_to_key(player_answer)):
                print("Oh noo answer is incorrect.. Game over!")
                reset_game_parameters()
                end_or_restart_game()

            elif question_number == total_questions_count:
                print("Game over. Congratulations You became a millionaire")
                reset_game_parameters()
                end_or_restart_game()
            else:
                print("Congratulations Your answer is correct! You already have: €" + str(prize))

            question_number += 1
            # call('cls', shell=True) not working...
