import curses
import string
import random
import time
import getch


def max_dimensions(window):
    height, width = window.getmaxyx()
    return height - 2, width - 1
def create_random_letter(window):
    width = max_dimensions(window)[1]
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(0, width)
    return 0, column, letter
def move_invaders(prev):
    new = {}
    for char, (row, column) in prev.items():
        new_row = row + 1
        new[char] = (new_row, column)
    return new

def draw_invaders(invaders, window):
    for char, (row, column) in invaders.items():
        height, width = max_dimensions(window)
        if row > height or column > width:
            continue
        window.addch(row, column, char)
def kill_invader(invaders, window, q):
    for char, (row, column) in invaders.items():
        if q == -1:
            if q == char:
                del invaders[char]
    return invaders
            
def main(window):
    curses.curs_set(0)
    invaders = {}    
    while True:
        window.clear()
        window.nodelay(True)
        q = window.getch()
        invaders = move_invaders(invaders)
        invader = create_random_letter(window)
        invaders[invader[2]] = (invader[0], invader[1])
        draw_invaders(invaders, window)
        kill_invader(invaders,window, q)
        time.sleep(0.4)
        window.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
