# Renograms
This is a Python text-based version of the Renograms game.

How to play:
  - The goal of the game is to fill the numbers 1-56 into the grid so that every consecutive number is adjacent vertically, horizontally, or diagonally.
  - For every puzzle, certain numbers in squares are marked with an asterisk. These numbers are set in position and cannot be changed. You can only place numbers in empty squares or squares occupied by a number without an asterisk
  - The numbers you have left to place are listed in the box titled: 'numbers to put in puzzle'. When this box is empty, you have filled all the squares.
  - To place a number in a square, type the column letter, then the row number right after (without a space). Then type a space and the number you want to place in this square.
    - e.g. to place the number 1 into square A1, type 'A1 1'
  - If you want to remove a number from a square you can enter 0 as your number.
    - e.g. to clear the number in square A1, type 'A1 0'
  - If you want to place a different number in a square, you can just type the square ID and the number. The number that was in the square will get placed back into the 'numbers to put in puzzle' list
  - If you want to clear the board of all non-asterisk squares, you can type CLEAR when asked for a square ID and number.
  - The puzzle will be complete when a continuous path from 1-56 can be drawn (i.e. every consecutive number is contained in one of the adjacently vertical, horizontal, or diagonal squares)

When prompted to type a square ID and number, you can also type the following:
  - Q to quit the puzzle
  - CLEAR to clear the board of all squares you have entered numbers into
  - HELP to bring up this help menu
