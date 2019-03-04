import letter_invader

def test_create_random_letter():
    width = 400
    height = 500
    window = height, width
    assert (letter_invader.create_random_letter(window)['r']  == (0, 300, 'r') for _ in range(0, 400)) 
    assert (letter_invader.create_random_letter(window)['s']  == (0, 200, 's') for _ in range(0, 400))

def test_move_invaders():
    height = 500
    assert (letter_invader.move_invaders({(0, 300):'r'}, window) == {(1, 300) : 'r'} for _ in range(0, height))
    assert (letter_invader.move_invaders({(501, 300):'r'}, window) == {(500, 300) : 'r'} for _ in range(0, height))

def test_draw_invaders():
    hieght = 500
    width = 500
    assert (letter_invader.draw_invaders({(3, 400) : 'd'}, window) == {(3, 400) : 'd'} for _ in range(0,500))
