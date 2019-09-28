import random, sys


def roller(argv):
    if len(argv) == 0:
        count = 1
        dice = 20
    elif len(argv) == 2:
        count = int(argv[0])
        dice = int(argv[1])
    else:
        return 'Argument error. Usage: roll [<count> <dice>]'

    results = []
    for i in range(count):
        results.append(random.randint(1, dice))

    # if count == 1:
    #     return f'Rolled {count}d{dice}: {results[0]}'

    return f'Rolled {count}d{dice}: {", ".join(map(str, results))}'


if __name__ == '__main__':
    print(roller(sys.argv[1:]))

