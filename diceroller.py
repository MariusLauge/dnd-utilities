import random, sys


def parser(argv):
    for roll in argv:
        if 'd' in roll:
            splt = roll.split('d')
            count = int(splt[0])
            dice = int(splt[1])
            res = []
            for i in range(count):
                res.append(random.randint(1, dice))
        else:
            print('Argument error. Usage: roll [<count>d<dice>]')

        print(f'{roll}: {", ".join(map(str, res))}')


if __name__ == '__main__':
    parser(sys.argv[1:])

