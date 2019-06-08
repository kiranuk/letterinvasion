"Import random module to get random choice and string to get ascii_lowercase"
import random
import string


def create_random_letter(width):
    "Create a letter in random columns with count zero"
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(0, width)
    count = 0
    return 0, column, letter, count


def move_invaders(invaders, height):
    "Move the letters downward"
    new = {}
    for (row, column), (char, count) in invaders.items():
        new_row = row + 1
        if new_row > height:
            new_row -= 1
        new[(new_row, column)] = (char, count)
    return new


def kill_invaders(invaders, user_input):
    "Kill the letter with user input initially change with '*'"
    list1 = []
    for (row, column), (char, count) in invaders.items():
        if char is user_input:
            track = (row, column)
            list1.append(track)
            continue
    if list1:
        invaders[max(list1)] = ("*", count)
    return invaders


def eliminating_char(invaders):
    "Eliminate '*' char by using count"
    del_char = []
    for (row, column), (char, count) in invaders.items():
        if "*" in char:
            invaders[(row, column)] = (char, count+1)
        if count == 3:
            del_char.append((row, column))
    if del_char:
        del invaders[del_char[0]]
    return invaders


def count_life(invaders, height):
    "Set-up the chances to miss the letter by applying life"
    life = 10
    for (row, column) in invaders.keys():
        max_row = height - 1
        if row > max_row:
            life -= 1
    return life
