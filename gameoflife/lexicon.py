from collections import namedtuple
import re

lexicon_regex = re.compile(
    r":(.+):\s*((?:.+\n)+?)((?:\s+[\.\*]+$)+)\n",
    flags=re.MULTILINE)

def cells_from_text_pattern(pattern, dead_cell='.', alive_cell='*'):
    alive_cells = []
    for i, line in enumerate(pattern):
        for j, char in enumerate(line):
            if char == alive_cell:
                alive_cells.append((j,i))
            elif char != dead_cell:
                raise ValueError("Unexpected character in pattern: " + char)
    return alive_cells

def parse(lexicon_text):
    lexicon = dict()
    matches = lexicon_regex.finditer(lexicon_text)
    for match in matches:
        name, description, cells_as_text = match.groups()
        description = " ".join(
            s.strip() for s in description.strip().splitlines())
        text_pattern = [l.strip() for l in cells_as_text.strip().splitlines()]
        item = LexiconItem(
            name,
            description,
            cells_from_text_pattern(text_pattern))
        lexicon[name] = item
    return lexicon

LexiconItem = namedtuple('LexiconItem', ['name', 'description', 'cells'])
