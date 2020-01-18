"""
This program is meant to train a user in solving log base 2 problems
Garrett Matthews
"""

import math
import random


def problem_generation(number,attachment):
    """Function to generate a log problem using a number, and an attachment"""
    num = random.choice(number)
    att = random.choice(attachment)
    answer = answer_generation(num, att)
    return (str(num)+att), answer


def answer_generation(number, attachment):
    """Function to find the answer of the generated log problem"""
    if attachment == " ":
        return math.log2(number)
    elif attachment == "K":
        return math.log2(number * 1000)
    elif attachment == "M":
        return math.log2(number * 1000000)
    elif attachment == "G":
        return math.log2(number * 1000000000)
    elif attachment == "T":
        return math.log2(number * 1000000000000)

def round_answer(number):
    dec = number % 1
    if dec >= 0.5:
        return int(number) + 1
    else:
        return int(number)


def main():
    number_lyst = [1, 2, 4, 8, 16, 32, 64, 128, 512]
    attach_lyst = [" ", "K", "M", "G", "T"]
    correct = 0
    print("As a reminder, all log problems presented are assumed to be log base 2", '\n')
    while correct < 5:
        problem, answer = problem_generation(number_lyst,attach_lyst)
        answer = round_answer(answer)
        prompt = ("{}{}{}".format("What is the log of ",problem," to the nearest integer? "))
        while True:
            try:
                response = int(input(prompt))
                break
            except:
                ValueError
            print("Please enter an integer")
        if response == answer:
            print("That is correct")
            correct += 1
            correct_string = ("{}{}".format(correct, " in a row CORRECT"))
            print(correct_string)
        else:
            wrong_string = ("{}{}".format("I'm sorry, that is incorrect. The answer is ", answer))
            print(wrong_string)
            correct = 0
            correct_string = ("{}{}".format("Correct count reset to ", correct))
            print(correct_string)
    print("Congratulations! You are super awesome! When it comes time to pick a team, I'll pick YOU")

if __name__ == "__main__":
    main()

