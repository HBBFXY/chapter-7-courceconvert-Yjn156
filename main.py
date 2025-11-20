PYTHON_KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
}

def convert_source_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    converted_lines = []
    for line in lines:
        tokens = []
        for token in line.split():
            if token in PYTHON_KEYWORDS:
                tokens.append(token)
            else:
                tokens.append(token.upper())
        converted_line = ' '.join(tokens) + '\n'
        converted_lines.append(converted_line)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(converted_lines)

convert_source_file('random_int.py', 'converted_random_int.py')
