import itertools

def neighbours(cell):
    x, y = cell
    return [(x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)]

class GameOfLife(object):

    def __init__(self, alive_cells=[]):
        self.alive_cells = alive_cells

    def is_alive(self, cell):
        return cell in self.alive_cells

    def alive_neighbours(self, cell):
        return [neighbour for neighbour in neighbours(cell)
                if self.is_alive(neighbour)]

    def zombie_cells(self):
        """
        Return the list of zombie cells.

        Zombie cells are cells that might become alive at the next iteration.
        Those cells are composed of all the cells that have at least
        one alive neighbour and aren't currently alive."""
        all_neighbours = set(itertools.chain.from_iterable(
            [neighbours(cell) for cell in self.alive_cells]))
        return all_neighbours - set(self.alive_cells)
