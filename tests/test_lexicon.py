from gameoflife import lexicon
from gameoflife.lexicon import LexiconItem
from nose.tools import *
import tempfile

def test_cells_from_text_pattern():
    pattern = """
.*.
..*
...""".strip().splitlines()
    cells = lexicon.cells_from_text_pattern(pattern)
    assert_items_equal(
        cells,
        ((1,0), (2,1))
    )

def test_cells_from_text_pattern_unexpected_char():
    pattern = """
.*o
..*
..."""
    with assert_raises(ValueError):
        lexicon.cells_from_text_pattern(pattern)

def test_parse_lexicon_no_content():
    empty_content = ""
    assert_items_equal(
        lexicon.parse(empty_content),
        []
    )

def test_parse_lexicon():
    test_content = """

:beehive: (p1)  The second most common {still life}.
	.**.
	*..*
	.**.

:bi-block: (p1)  The smallest {pseudo still life}.
	**.**
	**.**

"""
    gameoflife_lexicon = lexicon.parse(test_content)
    assert len(gameoflife_lexicon) == 2
    assert_equals(gameoflife_lexicon['beehive'], LexiconItem(
        name="beehive",
        description="(p1)  The second most common {still life}.",
        cells=[(1,0), (2,0), (0,1), (3,1), (1,2), (2,2)]
    ))
    assert_equals(gameoflife_lexicon['bi-block'], LexiconItem(
        name="bi-block",
        description="(p1)  The smallest {pseudo still life}.",
        cells=[(0,0), (1,0), (3,0), (4,0), (0,1), (1,1), (3,1), (4,1)]
    ))

