from os import popen
from json import load
from re import search, findall
from src.code_parser import augment_code
from src.reference import TESTS_PATH, JAVA_CODE_PATH


class CheeseSniffer:
    def __init__(self, code):
        self.code = code
        self.cheesy_tactics = []

    def sniff(self):
        self.cheesy_tactics = [
            len(findall('System.out.print', self.code)) > 1,
            search('for *\( *int *i *= *[0-1] *; *i *(<|<=) *(n|n *\+ *1) *; *(i\+\+|i *\+= *1)', self.code) is None,
            search('arr\[ *(i|i *\- *1) *] *= *(i *\* *i|\( *i *\+ *1 *\) *\* *\( *i *\+ *1 *\))', self.code) is None,
            search('System.out.println *\( *arr *\[ *(i|i *\- *1) *] *\)', self.code) is None,
            search('\{ *1 *, *4 *, *9 *, *16 *, *25 *}', self.code) is not None,
        ]

        return any(self.cheesy_tactics)


def run_tests():
    print("RUNNING TESTS")
    if first_test_is_valid() and not is_cheesy():
        augment_code()
        if multiple_tests_are_valid():
            print('Accepted.')


def multiple_tests_are_valid():
    print("Running multiple tests...")
    with open(TESTS_PATH, 'r') as file:
        tests = load(file)

    for i in range(1, 6):
        print(f'Running test #{i}')

        command = f'java {JAVA_CODE_PATH} {i * 5}'
        suggested_output = [int(line.rstrip('\n')) for line in popen(command, mode='r', buffering=-1)]

        if tests[f"{i}"] != suggested_output:
            print('Failed on test: ', i)
            return False

    return True


def first_test_is_valid():
    print('Examining solution...')
    command = f'java {JAVA_CODE_PATH}'

    suggested_output = [int(line.rstrip('\n')) for line in popen(command, mode='r', buffering=-1)]
    actual_output = [x ** 2 for x in range(1, 6)]

    print('Wrong answer\n' if suggested_output != actual_output else '', end='')

    return suggested_output == actual_output


def is_cheesy():
    with open(JAVA_CODE_PATH, 'r') as java_code:
        code = " ".join(java_code.readlines()).replace('\n', '')

    sniffer = CheeseSniffer(code)

    if sniffer.sniff():
        print('U r being cheesy :)')
        return True

    return False
