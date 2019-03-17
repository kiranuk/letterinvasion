import letter_invader
import random
import string

global height, width 
height, width = 500, 500
def test_move_invaders():
    assert letter_invader.move_invaders({(0, 300):'r'}, height) == {(1, 300) : 'r'}
    assert letter_invader.move_invaders({(400, 300):'r'}, height) == {(401, 300) : 'r'}

def test_kill_invaders():
    value = {(10, 50): 'd', (20, 30): 'k', (30,50): 'k', (100, 230): 'r', (25,25): 'j'}
    result = {(10, 50): 'd', (20, 30): 'k', (25, 25): 'j', (100, 230): 'r'}
    assert letter_invader.kill_invaders(value, 'k') == result
    assert letter_invader.kill_invaders(value, 'a') == value

def test_count_life():
    value = {(501,200): 'd', (200,200): 'e', (501,300): 'l',(300,200):'o'}
    result = 2
    assert letter_invader.count_life(value, 501) == result
