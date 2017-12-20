#!/usr/bin/python
#
# snake3.py shows how to move the snake.

import curses
import time

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

# The direction that the snake is traveling as delta for row and delta for col.
snake_drow = 0
snake_dcol = 1


def draw_board( screen, board ) :

	for linenr, row in enumerate( board ):
		line = "".join( row )
		screen.addstr( linenr+1, 0, line )


# We move the snake by adding a new head, and clearing its old tail (unless it needs to grow.)
# Returns True if the snake died because of the move.
def move_snake() :

	global snake_body

	# Figure out where the head of the snake will move to.
	head_row, head_col = snake_body[ 0 ]	# Current location.
	head_row += snake_drow
	head_col += snake_dcol

	# Did the snake eat its own body?
	if ( head_row, head_col ) in snake_body :
		return True

	# Re-assemble the body with a new head.
	snake_body = [ ( head_row, head_col ) ] + snake_body
	snake_body.pop()	# remove its old tail.

	# Did we hit the fence?
	if world[ head_row ][ head_col ] != ' ' :
		return True

	return False


def main( stdscr ):

	died = False

	while not died:
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

		# Now move the snake.
		died = move_snake()

		time.sleep( 0.2 )


curses.wrapper(main)

