#!/usr/bin/python
#
# snake1.py shows how to display a game board on the screen using curses.

import curses

# Our snake lives in a world of 15 rows of 25 characters.
world = [
	"+-----------------------+",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"|                       |",
	"+-----------------------+",
]

def draw_board( screen, board ) :

	for linenr, row in enumerate( board ):
		line = "".join( row )
		screen.addstr( linenr+1, 0, line )


def main( stdscr ):

	while True:
		stdscr.clear()
		stdscr.addstr( 0, 0, "Snake game. Ctrl-C to quit." )
		draw_board( stdscr, world )
		stdscr.refresh()

curses.wrapper(main)


