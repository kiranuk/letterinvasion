import curses
import string
import random
import time
import getch


def max_dimensions(window):
    height, width =   window.getmaxyx()
    return height - 1, width
def create_random_letter(window):
    width = max_dimensions(window)[1]
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(0, width)
    return 0, column, letter
def move_invaders(prev, window):
    new = {}
    for (row, column), char in prev.items():
        height, _ = max_dimensions(window)
        new_row = row + 1
        if new_row > height:
            new_row -= 1
        new[(new_row, column)] = char
    return new

def draw_invaders(invaders, window):
    for (row, column), char in invaders.items():
        height, width = max_dimensions(window)
    window.addch(row, column, char)
def kill_invader(letter, user_input):
    k = {}
    for char in invaders.values():
        user_input = getch.getch()
        if  char == user_input:
            k.replace(char, ' ')
    return k

#def life(invaders, window):
 #   lifeterm = 10
  #  if row > height or column > width:
   #     lifeterm -= 1

    #return lifeterm 


def main(window):
    curses.curs_set(0)
    invaders = {}
    while True:
        window.clear()
        invaders = move_invaders(invaders, window)
        invader = create_random_letter(window)
        invaders[(invader[0], invader[1])] = invader[2]
        draw_invaders(invaders, window)
        time.sleep(1.5)
        window.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
