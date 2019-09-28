import random, sys


def roller(argv):
    if len(argv) == 1:
        count = 1
        dice = 6
    elif len(argv) == 2:
        count = int(argv[0])
        dice = int(argv[1])
    else:
        return 'Argument error. Usage: roll [<count> <dice>]'

    results = []
    for i in range(count):
        results.append(random.randint(1, dice))

    if count == 1:
        return f'Rolled {count}d{dice}: {results[0]}'

    results_formatted = ''
    for x in results[:-1]:
        results_formatted += str(x) + ', '

    results_formatted += str(results[-1])
    return f'Rolled {count}d{dice}: {results_formatted}'


if __name__ == '__main__':
    print(roller(sys.argv[1:]))

