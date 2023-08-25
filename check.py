import re

errors: list[tuple[str, int, str]] = []

for name in ('emoji_category.txt', 'emoji_word.txt'):
    with open(f'opencc/{name}') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        match = re.match(r'(\S+)\t(\S+)( \S+)+', line)
        if not match or match.group(1) != match.group(2):
            errors.append((name, i + 1, line[:-1] if line.endswith('\n') else line))

if errors:
    print('Format error')
    for error in errors:
        print(f'{error[0]}:{error[1]} {error[2]}')
    exit(1)
