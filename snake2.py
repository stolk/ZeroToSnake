#!/usr/bin/python
#
# snake2.py adds a snake to the board.

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

# Our snake is defined as a list of coordinates (row,col) where its body is.
# We start as a snake of lenght 3, traveling to the right.
snake_body = [
	( 7,7 ), # The head on the right.
	( 7,6 ),
	( 7,5 ), # The tail on the left.
]


def draw_board( screen, board ) :

	for linenr, row in enumerate( board ):
		line = "".join( row )
		screen.addstr( linenr+1, 0, line )


def main( stdscr ):

	while True:
		stdscr.clear()
		stdscr.addstr( 0, 0, "Snake game. Ctrl-C to quit." )

		# Build up the board: start with a copy of the empty world.
		board = [ list(row) for row in world ]

		# Place the snake on our board.
		for idx, ( row, col ) in enumerate( snake_body ) :
			symbol = '#' if idx > 0 else 'O'
			board[ row ][ col ] = symbol

		# Now that we have set up the board, we should draw it on screen.
		draw_board( stdscr, board )
		stdscr.refresh()


curses.wrapper(main)

