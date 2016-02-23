from gameoflife import GameOfLife

def test_is_alive_alive_cell():
    game_of_life = GameOfLife(alive_cells=[(1,2),(3,4)])
    assert game_of_life.is_alive((1,2)) == True
    assert game_of_life.is_alive((3,4)) == True

def test_is_alive_dead_cell():
    game_of_life = GameOfLife(alive_cells=[(1,2),(3,4)])
    assert game_of_life.is_alive((1,1)) == False
