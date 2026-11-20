import random

WORDS = ["python", "git", "github", "snowman", "meltdown", "variable"]


def get_random_word():
    """Wählt ein zufälliges Wort aus der Liste."""
    return random.choice(WORDS)


if __name__ == "__main__":
    print("Welcome to Snowman Meltdown!")