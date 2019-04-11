"The letter invaders is used by curses, also time and game_setup imported as per needs"
import curses
import time
import game_setup


def max_dimensions(window):
    "Set-up window height and width"
    height, width = window.getmaxyx()
    return height - 2, width - 1


def draw_invaders(invaders, invader, window, count):
    "Prints to screen fallen letter"
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
    count = 0
    while True:
        window.clear()
        invader = game_setup.create_random_letter(width)
        invaders = game_setup.move_invaders(invaders, height)
        draw_invaders(invaders, invader, window, count)
        window.refresh()
        user_input = window.getch()
        game_setup.kill_invaders(invaders, user_input)
        game_setup.eliminating_char(invaders)
        time.sleep(0.9)
        window.clear()
        window.refresh()
        if user_input != -1:
            invaders = game_setup.kill_invaders(invaders, chr(user_input))
        if game_setup.count_life(invaders, height) == 0:
            break


if __name__ == '__main__':
    curses.wrapper(main)
