def DrawBoard(origArr, arr):
    print("     A    B    C    D    E    F    G    H")
    print("    ____ ____ ____ ____ ____ ____ ____ ____ ")
    counter = 0
    for i in range(7):
        print(i+1, " |", end="")
        for j in range(8):
            if arr[counter] == 0:
                print("    |", end="")
            elif arr[counter] < 10 and arr[counter] not in origArr:
                print("", arr[counter], " |", end="")
            elif arr[counter] < 10 and arr[counter] in origArr:
                print(" {}* |".format(arr[counter]), end="")
            elif arr[counter] >= 10 and arr[counter] in origArr:
                print(" {}*|".format(arr[counter]), end="")
            else:
                print("", arr[counter], "|", end="")
            counter += 1
        print("")
        print("   |____|____|____|____|____|____|____|____|")

def CheckSpace(origArr, col, row):
    # this function will check if the user entered a square that a number was automatically already placed in
    # need to convert the col (A=1, B=2, etc.) and row to integer
    # then calculate the position to check in the array that corresponds to this row and column
    # if the number is 0 or a number that does not exist in origArr, then return true, else return false
    column = ord(col) - 64
    row = int(row)
    pos = (row-1)*8 + column - 1
    if origArr[pos] != 0:
        print("Cannot insert into this space, a number has been entered here by default")
        return False
    return True

def ClearBoard(origArr, arr):
    for i in range(len(arr)):
        if arr[i] != origArr[i]:
            arr[i] = 0
    return arr

def UpdateBoard(arr, remains, col, row, num):
    column = ord(col) - 64
    row = int(row)
    number = int(num)
    pos = (row-1)*8 + column - 1
    if arr[pos] == 0 and number == 0:
        print("Nothing changed here")
        return arr, remains
    if arr[pos] != 0:
        # put the number back in the remains
        remains.append(arr[pos])
    if number != 0:
        remains.remove(number)
    remains.sort()
    arr[pos] = number
    return arr, remains

def CheckCompleted(remains, arr):
    # we haven't filled all the squares, so stop here
    if remains:
        return False
    arr2d = []
    #for item in arr:
        # no need to go through any more of this function if a zero is contained, the puzzle is obviously incomplete
    #    if item == 0:
    #        return False
    index_counter = 0
    for i in range(7):
        rowarr = []
        for j in range(8):
            rowarr.append(arr[index_counter])
            index_counter += 1
        arr2d.append(rowarr)
    row_index = 0
    col_index = 0
    for i in range(7):
        for j in range(8):
            if arr2d[i][j] == 1:
                row_index = i
                col_index = j
    new_row_index = 0
    new_col_index = 0
    for i in range(1, 55):
        counter = 0
        if i == 1:
            new_row_index = row_index
            new_col_index = col_index
        # edge case top left corner: check S, E, SE
        if row_index == 0 and col_index == 0:
            code = "TL"
            max_counter = 3
        # edge case bottom left corner: check N, E, NE
        elif row_index == 6 and col_index == 0:
            code = "BL"
            max_counter = 3
        # edge case top right corner: check W, S, SW
        elif row_index == 0 and col_index == 7:
            code = "TR"
            max_counter = 3
        # edge case bottom right corner: check N, W, NW
        elif row_index == 6 and col_index == 7:
            code = "BR"
            max_counter = 3
        # edge case top row: check W, SW, S, SE, E
        elif row_index == 0:
            code = "TOP"
            max_counter = 5
        # edge case bottom row: check W, NW, N, NE, E
        elif row_index == 6:
            code = "BOTTOM"
            max_counter = 5
        # edge case left column: N, NE, E, SE, S
        elif col_index == 0:
            code = "LEFT"
            max_counter = 5
        # edge case right column: S, SW, W, NW, N
        elif col_index == 7:
            code = "RIGHT"
            max_counter = 5
        # anything else can check all 8 neighbors
        else:
            code = "ALL"
            max_counter = 8
        # these codes help me to know which adjacent squares to check (to avoid going out of bounds)
        # check S
        if code in ["TL", "TR", "TOP", "LEFT", "RIGHT", "ALL"]:
            if arr2d[row_index+1][col_index] != i+1:
                counter += 1
            else:
                new_row_index = row_index + 1
        # check SW
        if code in ["TR", "TOP", "RIGHT", "ALL"]:
            if arr2d[row_index+1][col_index-1] != i+1:
                counter += 1
            else:
                new_row_index = row_index + 1
                new_col_index = col_index - 1
        # check W
        if code in ["TR", "TOP", "RIGHT", "BR", "BOTTOM", "ALL"]:
            if arr2d[row_index][col_index-1] != i+1:
                counter += 1
            else:
                new_col_index = col_index - 1
        # check NW
        if code in ["BR", "RIGHT", "BOTTOM", "ALL"]:
            if arr2d[row_index-1][col_index-1] != i+1:
                counter += 1
            else:
                new_row_index = row_index - 1
                new_col_index = col_index - 1
        # check N
        if code in ["BOTTOM", "BL", "BR", "LEFT", "RIGHT", "ALL"]:
            if arr2d[row_index-1][col_index] != i+1:
                counter += 1
            else:
                new_row_index = row_index - 1
        # check NE
        if code in ["LEFT", "BOTTOM", "BL", "ALL"]:
            if arr2d[row_index-1][col_index+1] != i+1:
                counter += 1
            else:
                new_row_index = row_index - 1
                new_col_index = col_index + 1
        # check E
        if code in ["TL", "BL", "BOTTOM", "TOP", "LEFT", "ALL"]:
            if arr2d[row_index][col_index+1] != i+1:
                counter += 1
            else:
                new_col_index = col_index + 1
        # check SE
        if code in ["TL", "TOP", "LEFT", "ALL"]:
            if arr2d[row_index+1][col_index+1] != i+1:
                counter += 1
            else:
                new_row_index = row_index + 1
                new_col_index = col_index + 1
        # if the square contains i+1, pass. we don't increment the counter, BUT update the next index to check
        # else, increment the counter. if the counter == max counter for the code, then we can return false since the next number is not in an adjacent square and the puzzle is incomplete
        if counter == max_counter:
            return False
        row_index = new_row_index
        col_index = new_col_index
    return True

def DisplayHelpMenu():
    print("\nHere is the help guide for Renograms!")
    print("How to play:")
    print("  - The goal of the game is to fill the numbers 1-56 into the grid so that every consecutive number is adjacent vertically, horizontally, or diagonally.")
    print("  - For every puzzle, certain numbers in squares are marked with an asterisk (*). These numbers are set in position and cannot be changed. You can only place numbers in empty squares or squares occupied by a number without an asterisk.")
    print("  - The numbers you have left to place are listed in the box titled: 'numbers to put in puzzle'. When this box is empty, you have filled all the squares.")
    print("  - To place a number in a square, type the column letter, then the row number right after (without a space). Then type a space and the number you want to place in this square.")
    print("     - e.g. to place the number 1 into square A1, type 'A1 1'")
    print("  - If you want to remove a number from a square you can enter 0 as your number.")
    print("     - e.g. to clear the number in square A1, type 'A1 0'")
    print("  - If you want to place a different number in a square, you can just type the square ID and the number. The number that was in the square will get placed back into the 'numbers to put in puzzle' list")
    print("  - If you want to clear the board of all non-asterisk squares, you can type CLEAR when asked for a square ID and number.")
    print("  - The puzzle will be complete when a continuous path from 1-56 can be drawn (i.e. every consecutive number is contained in one of the adjacently vertical, horizontal, or diagonal squares)")
    print("When prompted to type a square ID and number, you can also type the following:")
    print("  - Q to quit the puzzle")
    print("  - CLEAR to clear the board of all squares you have entered numbers into")
    print("  - HELP to bring up this help menu\n")

def PlayGame(arr):
    completed = False
    input2 = ""
    # keep track of the original array so that the user does not replace numbers that were automatically put in the puzzle to begin with
    origArr = []
    for i in range(len(arr)):
        origArr.append(arr[i])
    while not completed and input2 != 'Q':
        DrawBoard(origArr, arr)
        remains = []
        col = ""
        row = ""
        num = 0
        print("Numbers to put in puzzle: ", end="")
        for i in range(1, 56):
            if i not in arr:
                remains.append(i)
        print(remains)
        if input2 == "HELP":
            DisplayHelpMenu()
        valid = False
        while not valid:
            input2 = input("Enter the square you want to place a number in, followed by the number (e.g. H8 12):")
            if input2 in ['Q', "CLEAR", "HELP"]:
                valid = True
            elif len(input2) < 4:
                valid = False
            else:
                col = input2[0]
                row = input2[1]
                num = input2[3:]
                if col > 'H' or col < 'A':
                    valid = False
                    print("Error, invalid column")
                elif not row.isdigit():
                    valid = False
                    print("Error, invalid row")
                elif int(row) > 8 or int(row) < 1:
                    valid = False
                    print("Error, invalid row")
                elif not num.isdigit():
                    valid = False
                    print("Error, invalid number")
                elif int(num) > 56 or int(num) < 0:
                    valid = False
                    print("Error, invalid number")
                elif int(num) not in remains and int(num) != 0:
                    valid = False
                    print("Error, invalid number")
                elif not CheckSpace(origArr, col, row):
                    valid = False
                else:
                    valid = True
        if input2 == "CLEAR":
            arr = ClearBoard(origArr, arr)
        elif input2 == "HELP":
            pass
        elif input2 != 'Q':
            # to clear a square, the user should enter the square followed by a 0
            arr, remains = UpdateBoard(arr, remains, col, row, num)
        if not CheckCompleted(remains, arr):
            completed = False
        else:
            completed = True
    if completed:
        DrawBoard(origArr, arr)
        print("\nCONGRATULATIONS! You solved the puzzle!")

if __name__ == '__main__':
    print("Welcome to Renograms! Press P to start a new puzzle. Press Q to quit.")
    option = ""
    with open("puzzles.txt") as p:
        while option != 'Q':
            option = input("Enter:")
            if option == 'P':
                p.seek(0)
                content = p.readlines()
                for line in content:
                    print("Puzzle #", line[0:2])
                validPuzzle = False
                while not validPuzzle:
                    puzzleNum = input("Which puzzle would you like to play? (type the number): ")
                    if puzzleNum.isdigit() and 0 < int(puzzleNum) <= len(content):
                        validPuzzle = True
                c = content[int(puzzleNum)-1]
                a = c.split()
                b = []
                for i in range(1, len(a)):
                    b.append(int(a[i]))
                PlayGame(b)
                print("Would you like to play another puzzle? P to play, Q to quit.")
    p.close()