import itertools
from nose.tools import *
from gameoflife import *

def test_is_alive_alive_cell():
    game_of_life = GameOfLife(alive_cells=[(1,2),(3,4)])
    assert game_of_life.is_alive((1,2)) == True
    assert game_of_life.is_alive((3,4)) == True

def test_is_alive_dead_cell():
    game_of_life = GameOfLife(alive_cells=[(1,2),(3,4)])
    assert game_of_life.is_alive((1,1)) == False

def test_neighbours():
    assert_items_equal(
        neighbours((1,1)),
        [(0,0), (1,0), (2,0),
         (0,1),        (2,1),
         (0,2), (1,2), (2,2)]
    )

def test_alive_neighbours():
    game_of_life = GameOfLife(alive_cells=[(1,2),(2,0),(3,2)])
    assert_items_equal(
        game_of_life.alive_neighbours((1,1)),
        [(1,2),(2,0)]
    )

def test_zombie_cells_are_neighbours():
    game_of_life = GameOfLife(alive_cells=[(1,2),(2,0),(3,2)])
    all_neighbours = list(itertools.chain.from_iterable(
        [neighbours((1,2)), neighbours((2,0)), neighbours((3,2))]
    ))
    assert all(zombie in all_neighbours
               for zombie in game_of_life.zombie_cells())

def test_zombie_cells_are_all_dead():
    game_of_life = GameOfLife(alive_cells=[(1,2),(2,0),(3,2)])
    assert all(not game_of_life.is_alive(zombie)
               for zombie in game_of_life.zombie_cells())
