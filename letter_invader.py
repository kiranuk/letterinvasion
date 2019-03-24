import curses
import string
import random
import time


def max_dimensions(window):
    height, width = window.getmaxyx()
    return height - 2, width - 1


def create_random_letter(width):
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(0, width)
    return 0, column, letter


def move_invaders(invaders, height):
    new = {}
    for (row, column), char in invaders.items():
        new_row = row + 1
        if new_row > height:
            new_row -= 1
        new[(new_row, column)] = char
    return new


def draw_invaders(invaders, invader, window):
    invaders[(invader[0], invader[1])] = invader[2]
    for (row, column), char in invaders.items():
        if row > height or column > width:
            continue
        window.addch(row, column, char)


def kill_invaders(invaders, q):
    list1 = []
    for (row, column), char in invaders.items():
        if char is q:
            t = (row, column)
            list1.append(t)
            continue
    if list1:
        del invaders[max(list1)]
    return invaders


def count_life(invaders, height):
    count = 10
    for (row, column), char in invaders.items():
        max_row = height - 1
        if row > max_row:
            count -= 1
    return count


def main(window):
    curses.init_color(curses.COLOR_BLACK, 0, 0, 0)
    curses.init_color(curses.COLOR_WHITE, 1000, 1000, 1000)
    curses.curs_set(0)
    invaders = {}
    global height, width
    height, width = max_dimensions(window)
    t = 0.1
    window.nodelay(True)
    t += 0.1
    while True:
        window.clear()
        invader = create_random_letter(width)
        invaders = move_invaders(invaders, height)
        q = window.getch()
        draw_invaders(invaders, invader, window)
        window.refresh()
        kill_invaders(invaders, q)
        time.sleep(t)
        if q != -1:
            invaders = kill_invaders(invaders, chr(q))
        if count_life(invaders, height) == 0:
            break


if __name__ == '__main__':
    curses.wrapper(main)
