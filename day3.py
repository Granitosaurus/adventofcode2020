import math


def read_file():
    with open('day3.txt') as f:
        data = f.read().splitlines()
        return data


def first():
    data = read_file()
    x = 0
    counter = 0
    for i, y in enumerate(data):
        # if x is out range - wrap around
        if x >= len(y):
            x = x - len(y)
        if y[x] == '#':
            counter += 1
        x += 3
    print(f'pattern 3, 1 will encounter {counter} trees')


def second():
    data = read_file()
    PATTERNS = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    trees_hit = []
    for right, down in PATTERNS:
        x = 0
        counter = 0
        for i, y in enumerate(data):
            if not (i % down == 0):
                continue
            # if x is out range - wrap around
            if x >= len(y):
                x = x - len(y)
            if y[x] == '#':
                counter += 1
            x += right
        trees_hit.append(counter)
        print(f'pattern {right}, {down} will encounter {counter} trees')
    print(f'total pattern tree encounter product: {math.prod(trees_hit)}')


if __name__ == '__main__':
    first()
    print('-' * 80)
    second()
