import pygame, sys
from pygame.locals import *
from model import gameoflife
import lexicon as lex
import sys

next_step_event = pygame.USEREVENT + 1
refresh_rate_ms = 500

white = (255,255,255)
black = (0,0,0)

cell_size = 30
cell_border = black

width, height = 900, 600

with open('./lexicon.txt', 'r') as f:
    lexicon_text = f.read()
    lexicon = lex.parse(lexicon_text)

def main():
    try:
        figure_name = sys.argv[1]
    except IndexError:
        print_usage()
    game_of_life = gameoflife(initial_cells=lexicon[sys.argv[1]].cells)
    state = next(game_of_life)

    pygame.init()

    # Program the next step event to trigger repeatedly.
    pygame.time.set_timer(next_step_event, refresh_rate_ms)

    screen = pygame.display.set_mode((width, height), 0, 32)

    while True:
        for event in pygame.event.get():
            if event.type == next_step_event:
                state = next(game_of_life)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        draw_game(screen, state)
        pygame.display.update()

def draw_game(screen, state):
    screen.fill(white)
    for i in xrange(0, width / cell_size, 1):
        for j in xrange(0, height / cell_size, 1):
            cell = (i, j)
            # Width of 0 means we fill the entire cell.
            cell_width = 0 if state.is_alive(cell) else 1
            pygame.draw.rect(
                screen,
                cell_border,
                (i * cell_size, j * cell_size, cell_size, cell_size),
                cell_width)

def print_usage():
    print "Usage: python gameoflife/ui.py <figure-name>"
    print "Where <figure-name> is one the figures from 'lexicon.txt'"
    sys.exit(1)

if __name__ == '__main__':
    main()
