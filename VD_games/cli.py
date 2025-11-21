
def welcome_user():
    """Welcome the user and return their name."""
    print("May I have your name? ", end="")
    name = input().strip()
    print(f"Hello, {name}!")
    return name
