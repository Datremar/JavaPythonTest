from os import path
from json import dump
from src.reference import TESTS_PATH


def generate_tests():
    if not path.exists(TESTS_PATH):
        with open(TESTS_PATH, 'w') as file:
            tests = {}

            for y in range(1, 11):
                tests[y] = [x ** 2 for x in range(1, y * 5 + 1)]

            dump(tests, file)
