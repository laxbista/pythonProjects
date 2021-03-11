from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, answer, turns):
    """Checks answers with user's guess and returns number of attempts remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}")


def set_level():
    """Sets difficulty level"""
    level = input("Type 'e' for easy or 'h' for hard level: ")
    if level == "e":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(logo)
    print("Welcome to Number Guessing Game\nChoose a number between 1 to 100.")
    answer = randint(1, 100)
    turns = set_level()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses. You Lose")
            return
        elif guess != answer:
            print("Guess Again")


game()
