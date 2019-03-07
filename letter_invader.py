import curses
import string
import random
import time



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
    for (row, column), char in prev.items():
        new_row = row + 1
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
            
def main(window):
    curses.curs_set(0)
    invaders = {}    
    while True:
        window.clear()
        window.nodelay(True)
        invaders = move_invaders(invaders)
        invader = create_random_letter(window)
        invaders[(invader[0], invader[1])] = invader[2]
        draw_invaders(invaders, window)
        q = window.getch()
        kill_invader(invaders, q)
        time.sleep(0.4)
        window.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
