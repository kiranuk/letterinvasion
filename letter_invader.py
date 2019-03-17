import curses
import string
import random
import time
from collections import Counter

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
    count = 0
    for (row, column), char in invaders.items(): 
        max_row = height - 1
        if row > max_row:
            count += 1
    return count

def display_life(window):
    #v = count_life(invaders, height)
    char = ':<12'
    window.hline(height-2, width-2, ord(char))

def main(window):
    curses.curs_set(0)
    invaders = {}
    global height, width
    height, width = max_dimensions(window)
    t = 0.3
    window.nodelay(True)
    t += 0.1
    while True:
        window.clear()
        invader = create_random_letter(width)
        invaders = move_invaders(invaders, height)
        q = window.getch()
        draw_invaders(invaders, invader, window)
        display_life(window)
        window.refresh()
        kill_invaders(invaders, q)
        time.sleep(t)
        if q != -1:
            invaders = kill_invaders(invaders,chr(q))
        if count_life(invaders, height) == 10:
            
            break
        window.refresh()
if __name__ == '__main__':
    curses.wrapper(main)
    #init = {(300,20): 'g',(400,200): 'k',(500,300): 'k',(200,100): 'g'}
    #kill_invaders(init, 'k')

