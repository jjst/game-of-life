Game Of Life 
============

This is a simple implementation of [Conway's Game Of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in
Python using [Pygame](http://www.pygame.org/).

It loads and displays figures from the [Life Lexicon](http://www.argentum.freeserve.co.uk/lex_home.htm).

![Sample run](https://i.imgur.com/WeMmh6E.gif)

Requirements 
------------

The program requires [Python 2.7](https://www.python.org/), which is typically pre-installed under Linux OS'es and can
be easily installed on others.  It also depends on [Pygame](http://www.pygame.org/). The easiest way to install Pygame
under most Linux versions is to use the pre-packaged version from the repositories. For example, on Ubuntu:

```bash 
$ sudo apt-get install python-pygame
```

Or on Fedora:

```bash
$ sudo dnf install pygame
```

Running 
-------

To run the game of life, clone the project, cd to the cloned location, and run ui.py, passing a game of life figure as
an argument:

```bash 
$ git clone https://github.com/jjst/game-of-life.git
$ cd game-of-life/ 
$ python gameoflife/ui.py spaceship 
```

The list of available figures is read from `lexicon.txt`. This plain text file, courtesy of [The Life
Lexicon](http://www.argentum.freeserve.co.uk/lex_home.htm) from Stephen Silver, contains a list of every Game Of Life
figure along with a description. Peek in there to see which figures can be loaded.
