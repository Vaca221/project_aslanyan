#!/usr/bin/env python3

import prompt
from VD_games.games import even, calc, gcd


def main():
    print("Welcome to the VD Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    
    print("Choose a game:")
    print("1 - Even Number")
    print("2 - Calculator") 
    print("3 - Greatest Common Divisor")
    
    choice = prompt.string("Enter your choice (1-3): ")
    
    if choice == '1':
        from VD_games.engine import run_game
        run_game(even)
    elif choice == '2':
        from VD_games.engine import run_game
        run_game(calc)
    elif choice == '3':
        from VD_games.engine import run_game
        run_game(gcd)
    else:
        print("Invalid choice!")


if __name__ == '__main__':
    main()
