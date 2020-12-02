def read_data():
    with open('day1.txt') as f:
        data = [int(num) for num in f.read().splitlines() if num]
    return data


def first():
    data = read_data()
    for number in data:
        for add in data:
            if number + add == 2020:
                print(number)
                print(add)
                print(number * add)


def second():
    data = read_data()
    for number in data:
        for add in data:
            for third in data:
                if number + add + third == 2020:
                    print(number)
                    print(add)
                    print(third)
                    print(number * add * third)


if __name__ == '__main__':
    first()
    second()
