from src.code_parser import get_code
from tests.test_generator import generate_tests
from tests.tests import run_tests
from sys import argv


def main():
    _, path = argv

    generate_tests()
    get_code(path)
    run_tests()


if __name__ == '__main__':
    main()
