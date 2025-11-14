"""Main VD games package script."""

from VD_games.cli import welcome_user


def main():
    """Run the main VD games program."""
    print("Welcome to the VD-games!")
    name = welcome_user()
    print(f"Hello, {name}! This is the main VD games package.")
