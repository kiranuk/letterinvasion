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

def move_invaders(invaders, window):
    new = {}
    for (row, column), char in invaders.items():
        height, _ = max_dimensions(window)
        new_row = row + 1
        if new_row > height:
            new_row -= 1 
        new[(new_row, column)] = char
    return new

def draw_invaders(invaders, window):
    for (row, column), char in invaders.items():
        height, width = max_dimensions(window)
        if row > height or column > width:
            continue
        window.addch(row, column, char)

def kill_invader(invaders, q):
    invaders = {key: value for key, value in invaders.items() if value is not q}
    return invaders

def count_life(invaders, height):
    life = 10
    max_row = height - 1
    for (row, column) in invaders.keys():
        if (max_row, column):
            life -= 1
    return life


def main(window):
    curses.curs_set(0)
    invaders = {}    
    while True:
        window.clear()
        window.nodelay(True)
        height, width = max_dimensions(window)
        invader = create_random_letter(width)
        invaders = move_invaders(invaders, window)
        invaders[(invader[0], invader[1])] = invader[2]
        q = window.getch()
        draw_invaders(invaders, window)
        window.refresh()
        kill_invader(invaders, q)
        count_life(invaders, height)
        time.sleep(0.4)
        window.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
