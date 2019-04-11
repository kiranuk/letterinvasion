import curses
import time
import game_setup


def max_dimensions(window):
    height, width = window.getmaxyx()
    return height - 2, width - 1


def draw_invaders(invaders, invader, window, count):
    invaders[(invader[0], invader[1])] = (invader[2], count)
    for (row, column), (char, count) in invaders.items():
        if row > height or column > width:
            continue
        window.addch(row, column, char)


def main(window):
    curses.init_color(curses.COLOR_BLACK, 0, 0, 0)
    curses.curs_set(0)
    invaders = {}
    global height, width
    height, width = max_dimensions(window)
    window.nodelay(True)
    lag = 0
    count = 0
    while True:
        # if lag == 3:
        #     invader
        #     lag = 0
        # lag += 1
        window.clear()
        invader = game_setup.create_random_letter(width)
        invaders = game_setup.move_invaders(invaders, height)
        draw_invaders(invaders, invader, window, count)
        window.refresh()
        q = window.getch()
        game_setup.kill_invaders(invaders, q)
        game_setup.eliminating_char(invaders)
        time.sleep(0.9)
        window.clear()
        window.refresh()
        if q != -1:
            invaders = game_setup.kill_invaders(invaders, chr(q))
        
        if game_setup.count_life(invaders, height) == 0:
            break


if __name__ == '__main__':
    curses.wrapper(main)
