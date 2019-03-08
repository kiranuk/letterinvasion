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

def draw_invaders(invaders, window):
    for (row, column), char in invaders.items():
        if row > height or column > width:
            continue
        window.addch(row, column, char)

def kill_invader(invaders, q):
    invaders = {key: value for key, value in invaders.items() if value is not q}
    return invaders

def count_life(invaders, height):
    life = 10
    max_row = height - 1
    for (row, column), char in invaders.items():
        if max_row == row:
            life -= 1
    return life


def main(window):
    curses.curs_set(0)
    invaders = {}
    global height, width
    height, width = max_dimensions(window)
    while True:
        window.clear()
        window.nodelay(True)
        invader = create_random_letter(width)
        invaders = move_invaders(invaders, height)
        invaders[(invader[0], invader[1])] = invader[2]
        q = window.getch()
        if q != -1:
            invaders = kill_invader(invaders, chr(q))
        draw_invaders(invaders, window)
        window.refresh()
        kill_invader(invaders, q)
        time.sleep(0.4)
        window.refresh()
        if count_life(invaders, height) == 0:
            break

if __name__ == '__main__':
    curses.wrapper(main)
