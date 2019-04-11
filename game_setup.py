import random
import string


def create_random_letter(width):
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(0, width)
    count = 0
    return 0, column, letter, count


def move_invaders(invaders, height):
    new = {}
    for (row, column), (char, count) in invaders.items():
        new_row = row + 1
        if new_row > height:
            new_row -= 1
        new[(new_row, column)] = (char, count)
    return new


def kill_invaders(invaders, q):
    list1 = []
    for (row, column), (char, count) in invaders.items():
        if char is q:
            t = (row, column)
            list1.append(t)
            continue
    if list1:
        invaders[max(list1)] = ("*", count)
    return invaders

def eliminating_char(invaders):
    del_char = []
#    while True:
    for (row, column), (char, count) in invaders.items():
        if "*" in char:
            invaders[(row, column)] = (char, count+1)
        if count == 3:
            del_char.append((row, column))
    if del_char:
        del invaders[del_char[0]]
            #del_char.clear()
        #print(del_char)
    #print(invaders)
        #count += 1
    return invaders
            #count = 0
#       return invaders


#def single_letter_display(invader):


def count_life(invaders, height):
    life = 10
    for (row, column), (char, count) in invaders.items():
        max_row = height - 1
        if row > max_row:
            life -= 1
    return life

# if __name__ == '__main__':
#     invaders = {(10, 50): ('d', 0),
#                 (20, 60): ('k', 0),
#                (40, 50): ('*', 0),
#                (100, 230): ('r', 0),
#                (25, 25): ('j', 0)}
#     list1 = (40, 50)
    #kill_invaders(invaders, 'k')
#    eliminating_char(invaders)
