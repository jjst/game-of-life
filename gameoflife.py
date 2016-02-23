
class GameOfLife(object):

    def __init__(self, alive_cells=[]):
        self.alive_cells = alive_cells

    def is_alive(self, cell):
        return cell in self.alive_cells
