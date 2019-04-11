import game_setup
import random
import string


global height, width
height, width = 500, 500


def test_move_invaders():
    assert game_setup.move_invaders({(0, 300):('r', 1)}, height) == {(1, 300) : ('r', 1)}
    assert game_setup.move_invaders({(400, 300):('r', 1)}, height) == {(401, 300) : ('r', 1)}


def test_kill_invaders():
    value = {(10, 50): ('d', 0),
             (20, 30): ('k', 0),
             (40, 50): ('k', 0),
             (100, 230): ('r', 0),
             (25, 25): ('j', 0)}

    result = {(10, 50): ('d', 0),
             (20, 30): ('k', 0),
             (40, 50): ('*', 0),
             (100, 230): ('r', 0),
             (25, 25): ('j', 0)}
    assert game_setup.kill_invaders(value, 'k') == result
    assert game_setup.kill_invaders(value, 'a') == value

def test_eliminating_char():
    value = {(10, 50): ('d', 0),
             (20, 30): ('k', 0),
             (40, 50): ('*', 0),
             (100, 230): ('r', 0),
             (25, 25): ('j', 0)}
    update_value =  {(10, 50): ('d', 0),
             (20, 30): ('k', 0),
             (40, 50): ('*', 1),
             (100, 230): ('r', 0),
             (25, 25): ('j', 0)}
    updat_value1 =  {(10, 50): ('d', 0),
             (20, 30): ('k', 0),
             (40, 50): ('*', 2),
             (100, 230): ('r', 0),
             (25, 25): ('j', 0)}

    result = {(10, 50): ('d', 0),
             (20, 30): ('k', 0),
             (100, 230): ('r', 0),
             (25, 25): ('j', 0)}
    assert game_setup.eliminating_char(value) == update_value 
    assert game_setup.eliminating_char(updat_value1) == result

def test_count_life():
    value = {(501, 200): ('d', 0), (200, 200): ('e', 0), (501, 300): ('l', 0), (300, 200): ('o', 0)}
    result = 8
    assert game_setup.count_life(value, 501) == result
