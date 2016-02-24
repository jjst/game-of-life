import itertools
from nose.tools import *
from gameoflife.model import *

def test_is_alive_alive_cell():
    step = GameOfLifeStep(alive_cells=[(1,2),(3,4)])
    assert step.is_alive((1,2)) == True
    assert step.is_alive((3,4)) == True

def test_is_alive_dead_cell():
    step = GameOfLifeStep(alive_cells=[(1,2),(3,4)])
    assert step.is_alive((1,1)) == False

def test_is_dead_alive_cell():
    step = GameOfLifeStep(alive_cells=[(1,2),(3,4)])
    assert step.is_dead((1,2)) == False

def test_is_dead_dead_cell():
    step = GameOfLifeStep(alive_cells=[(1,2),(3,4)])
    assert step.is_dead((1,1)) == True

def test_neighbours():
    assert_items_equal(
        neighbours((1,1)),
        [(0,0), (1,0), (2,0),
         (0,1),        (2,1),
         (0,2), (1,2), (2,2)]
    )

def test_alive_neighbours():
    step = GameOfLifeStep(alive_cells=[(1,2),(2,0),(3,2)])
    assert_items_equal(
        step.alive_neighbours((1,1)),
        [(1,2),(2,0)]
    )

def test_zombie_cells_are_neighbours():
    step = GameOfLifeStep(alive_cells=[(1,2),(2,0),(3,2)])
    all_neighbours = neighbours((1,2)) + neighbours((2,0)) + neighbours((3,2))
    assert_items_equal(step.zombie_cells(), set(all_neighbours))

def test_zombie_cells_are_all_dead():
    step = GameOfLifeStep(alive_cells=[(1,2),(1,1),(2,1)])
    assert all(step.is_dead(zombie)
               for zombie in step.zombie_cells())

def test_next_step_cell_with_no_neighbours_dies():
    step = GameOfLifeStep(alive_cells=[(1,2)])
    next_step = step.next_step()
    assert (1,2) not in next_step.alive_cells

def test_next_step_cell_with_one_neighbours_dies():
    step = GameOfLifeStep(alive_cells=[(1,2), (1,1)])
    next_step = step.next_step()
    assert (1,1) not in next_step.alive_cells
    assert (1,2) not in next_step.alive_cells

def test_next_step_cell_with_2_neighbours_survives():
    step = GameOfLifeStep(alive_cells=[(0,1), (1,1), (2,1)])
    next_step = step.next_step()
    assert (1,1) in next_step.alive_cells

def test_next_step_cell_with_3_neighbours_survives():
    step = GameOfLifeStep(alive_cells=[(0,1), (1,1), (2,1), (1,0)])
    next_step = step.next_step()
    assert (1,1) in next_step.alive_cells

def test_next_step_cell_with_over_3_neighbours_dies():
    step = GameOfLifeStep(alive_cells=[(0,1), (1,1), (2,1), (1,0), (2,0)])
    next_step = step.next_step()
    assert (1,1) not in next_step.alive_cells

def test_next_dead_cell_with_3_alive_neighbours_becomes_alive():
    step = GameOfLifeStep(alive_cells=[(0,1), (1,1), (2,1)])
    next_step = step.next_step()
    assert_in((1,0), next_step.alive_cells)
    assert_in((1,2), next_step.alive_cells)

def test_gameoflife_should_first_return_initial_step():
    initial_cells = [(0,1), (1,1)]
    assert_equal(
        next(gameoflife(initial_cells)),
        GameOfLifeStep(alive_cells=initial_cells)
    )

def test_gameoflife_should_return_next_steps():
    initial_cells = [(0,1), (1,1)]
    initial_step = GameOfLifeStep(initial_cells)
    next_step = initial_step.next_step()
    game = gameoflife(initial_cells)
    next(game) # Skip initial step
    assert next(game) == next_step
