"""Core game logic for Snowman Meltdown."""

import random

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Select a random word from the word list."""
    return random.choice(WORDS)


def build_word_display(secret_word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage and the current word progress."""
    print(STAGES[mistakes])
    print("Word:", build_word_display(secret_word, guessed_letters))
    print()


def get_valid_guess(guessed_letters):
    """Ask until the user enters a single new letter, then return it."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def is_word_guessed(secret_word, guessed_letters):
    """Return True if every letter of the word has been guessed."""
    return all(letter in guessed_letters for letter in secret_word)


def play_game():
    """Run one round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

        if is_word_guessed(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations, you saved the snowman!")
            break

        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Game Over! The word was:", secret_word)
            break