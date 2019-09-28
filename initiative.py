import sys, tty, termios
import config
from collections import OrderedDict
from os import system
from itertools import cycle
from string import capwords


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def print_commas(l, msg=None):
    if msg:
        print(msg, ", ".join(map(str, l)))
    else:
        print(", ".join(map(str, l)))


def names(characters):
    while True:
        system('clear')
        print_commas(characters, 'Characters so far: ')
        print('Add another character to initiative? (y/n)')
        cont = getch()
        if cont == 'y':
            name = input('Input name of character: ')
            characters.add(capwords(name.lower()))
        if cont == 'n':
            break
        if cont == 'q':
            break
    return characters


def iniative(characters):
    for character in characters:
        system('clear')
        print_commas(characters)
        initiative_value = input(f'Please input initiative for {character}: ')

        while not initiative_value.isdigit():
            initiative_value = input('Please input a digit! ')
        characters[character] = int(initiative_value)

    return characters


def main(argv):
    system('clear')
    players = set()
    if len(argv) == 1:
        if argv[0].lower() == 'list':
            print_commas(config.PLAYERS, 'Existing configs: ')
        if argv[0].lower() in config.PLAYERS:
            players = config.PLAYERS[argv[0].lower()]
            print_commas(players, f'Players loaded from config:\n"{argv[0].lower().capitalize()}"')
        else:
            input('Player config not found!')

    characters = OrderedDict((n, 0) for n in names(players))
    init = iniative(characters)

    # Main loop
    while True:
        order = OrderedDict(sorted(init.items(), key=lambda t: -t[1]))
        if len(order) == 0:
            return

        for current in cycle(order):
            system('clear')
            print('             *** INITIATIVE ***             ')
            print(' - - - - - - - - - - - - - - - - - - - - - -')

            for name in order.keys():
                if name == current:
                    print(f'--> {order[name]:2} | {name}')
                else:
                    print(f'    {order[name]:2} | {name}')
            print(' - - - - - - - - - - - - - - - - - - - - - -')
            print(' j - next | i - add | x - remove | q - exit')

            inp = getch()
            while inp not in {'i', 'j', 'x', 'q'}:
                inp = getch()
            if inp == 'q':
                return
            elif inp == 'j':
                continue
            elif inp == 'i':
                name = input('Input name of character: ')
                name = capwords(name.lower())
                initiative_value = input(f'Please input initiative for {name}: ')
                while not initiative_value.isdigit():
                    initiative_value = input('Please input a digit! ')
                init[name] = int(initiative_value)
                break
            elif inp == 'x':
                del init[current]
                break


if __name__ == '__main__':
    main(sys.argv[1:])
