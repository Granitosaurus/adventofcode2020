def read_file():
    with open('day2.txt') as f:
        data = f.read().splitlines()
        return [line.split(': ') for line in data]


def first():
    rules = read_file()
    counter = 0
    for rule, password in rules:
        count, letter = rule.split(' ')
        cmin, cmax = count.split('-')
        valid_range = list(range(int(cmin), int(cmax) + 1))
        if password.count(letter) in valid_range:
            print(rule, password)
            counter += 1
    print(counter)

def second():
    rules = read_file()
    counter = 0
    for rule, password in rules:
        count, letter = rule.split(' ')
        pos1, pos2 = (int(v)-1 for v in count.split('-'))
        try:
            if (password[pos1] == letter and password[pos2] != letter) or (
                    password[pos2] == letter and password[pos1] != letter
            ):
                counter += 1
                print(rule, password)
        except IndexError:
            continue
    print(counter)


if __name__ == '__main__':
    second()
