
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
