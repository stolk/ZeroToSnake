#!/usr/bin/python
#
# snake4.py adds food to the board.

import curses
import time
import random

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

food = ( 7,20 )


def draw_board( screen, board ) :

	for linenr, row in enumerate( board ):
		line = "".join( row )
		screen.addstr( linenr+1, 0, line )


# We move the snake by adding a new head, and clearing its old tail (unless it needs to grow.)
# Returns True if the snake died because of the move.
def move_snake() :

	global snake_body
	global food

	# Figure out where the head of the snake will move to.
	head_row, head_col = snake_body[ 0 ]	# Current location.
	head_row += snake_drow
	head_col += snake_dcol

	# Did the snake eat its own body?
	if ( head_row, head_col ) in snake_body :
		return True

	# Did the snake eat the food?
	ate_food = ( head_row, head_col ) == food

	if ate_food :
		# Spawn new food at a random location on the board.
		food = ( int(random.uniform(1,15)), int(random.uniform(1,24) ) )

	# Re-assemble the body with a new head.
	snake_body = [ ( head_row, head_col ) ] + snake_body
	if not ate_food :
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

		# Place the food on the board.
		board[ food[0] ][ food[1] ] = '*'

		# Now that we have set up the board, we should draw it on screen.
		draw_board( stdscr, board )
		stdscr.refresh()

		# Now move the snake.
		died = move_snake()

		time.sleep( 0.2 )


curses.wrapper(main)

