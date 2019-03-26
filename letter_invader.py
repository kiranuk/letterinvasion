import curses
import time
import game_setup


def max_dimensions(window):
    height, width = window.getmaxyx()
    return height - 2, width - 1


def draw_invaders(invaders, invader, window):
    invaders[(invader[0], invader[1])] = invader[2]
    for (row, column), char in invaders.items():
        if row > height or column > width:
            continue
        window.addch(row, column, char)


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
        invader = game_setup.create_random_letter(width)
        invaders = game_setup.move_invaders(invaders, height)
        q = window.getch()
        draw_invaders(invaders, invader, window)
        window.refresh()
        game_setup.kill_invaders(invaders, q, t)
        time.sleep(t)
        if q != -1:
            invaders = game_setup.kill_invaders(invaders, chr(q), t)
        if game_setup.count_life(invaders, height) == 0:
            break


if __name__ == '__main__':
    curses.wrapper(main)
