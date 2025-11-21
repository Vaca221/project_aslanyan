import random

DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def is_even(number):
    """Проверяет, является ли число чётным"""
    return number % 2 == 0


def generate_round():
    """
    Генерирует один раунд для игры Чётное число
    """
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    
    return question, correct_answer


# Убедитесь, что нет лишнего кода после этой строки
