from src.reference import JAVA_CODE_PATH


def get_code(path: str):
    with open(path, 'r') as java_file:
        with open(JAVA_CODE_PATH, 'w') as code:
            code.writelines(list(java_file))


def augment_code():
    with open(JAVA_CODE_PATH, 'r') as code:
        lines = code.readlines()

        for i in range(len(lines)):
            if lines[i].startswith('//'):
                lines[i] = ''

            if 'int n = 5;' in lines[i]:
                lines[i] = '      int n = Integer.parseInt(args[0]);\n'

    with open(JAVA_CODE_PATH, 'w') as code:
        code.writelines(lines)



