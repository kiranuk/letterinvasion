import letter_invader
import random
import string

global height, width 
height, width = 500, 500
def test_create_random_letter():
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(0, 500)
    assert (letter_invader.create_random_letter(width)  == 0, column, letter) 
    assert (letter_invader.create_random_letter(width)  == 0, column, letter)

def test_move_invaders():
    assert letter_invader.move_invaders({(0, 300):'r'}, height) == {(1, 300) : 'r'}
    assert letter_invader.move_invaders({(400, 300):'r'}, height) == {(401, 300) : 'r'}

def test_kill_invader():
    value = {(10, 50): 'd', (20, 30): 'k', (100, 230): 'r', (25,25): 'j'}
    result = {(10, 50): 'd', (25, 25): 'j', (100, 230): 'r'}
    assert letter_invader.kill_invader(value, 'k') == result
    assert letter_invader.kill_invader(value, 'a') == value

def test_count_life():
    value = {(500,200): 'd'}
    result = 9
    assert letter_invader.count_life(value, 501) == result
