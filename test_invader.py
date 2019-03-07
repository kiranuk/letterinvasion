import letter_invader
import random
import string

def test_create_random_letter():
    width = 400
    letter = random.choice(string.ascii_lowercase)
    column = random.randrange(0,400)
    assert (letter_invader.create_random_letter(width)  == 0, column, letter) 
    assert (letter_invader.create_random_letter(width)  == 0, column, letter)

def test_move_invaders():
    height = 500
    assert (letter_invader.move_invaders({(0, 300):'r'}) == {(1, 300) : 'r'})
    assert (letter_invader.move_invaders({(400, 300):'r'}) == {(401, 300) : 'r'})

def test_draw_invaders():
    height = 500
    width = 500
    assert (letter_invader.draw_invaders({(3, 400) : 'd'}, window) == {(3, 400) : 'd'} for _ in range(0, 500))

def test_kill_invader():
    value = {(10, 50): 'd', (20, 30): 'k', (100, 230): 'r', (25,25): 'j'}
    result = {(10, 50): 'd', (25, 25): 'j', (100, 230): 'r'}
    assert (letter_invader.kill_invader(value, 'k') == result)
    assert (letter_invader.kill_invader(value, 'a') == value) 
