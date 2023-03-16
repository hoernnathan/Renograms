def DrawBoard(arr):
    print("     A    B    C    D    E    F    G    H")
    print("    ____ ____ ____ ____ ____ ____ ____ ____ ")
    counter = 0
    for i in range(7):
        print(i+1, " |", end="")
        for j in range(8):
            if arr[counter] == 0:
                print("    |", end="")
            elif arr[counter] < 10:
                print("", arr[counter], " |", end="")
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
    column = ord(col) - 65
    row = int(row)
    pos = ((row-1)*8-1) + column
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
    column = ord(col) - 65
    row = int(row)
    number = int(num)
    pos = ((row - 1) * 8 - 1) + column
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

def CheckCompleted(arr):
    arr2d = []
    for item in arr:
        # no need to go through any more of this function if a zero is contained, the puzzle is obviously incomplete
        if item == 0:
            return False
    for i in range(7):
        rowarr = []
        for j in range(8):
            rowarr.append(arr[j])
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
        max_counter = 0
        code = ""
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
        # TODO: these codes help me to know which adjacent squares to check (to avoid going out of bounds)
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

def PlayGame(arr):
    #print(arr)
    completed = False
    input2 = ""
    # keep track of the original array so that the user does not replace numbers that were automatically put in the puzzle to begin with
    origArr = arr
    while not completed and input2 != 'Q':
        DrawBoard(arr)
        remains = []
        col = ""
        row = ""
        num = 0
        print("Numbers to put in puzzle: ", end="")
        for i in range(1, 56):
            if i not in arr:
                remains.append(i)
        print(remains)
        valid = False
        while not valid:
            input2 = input("Enter the square you want to place a number in, followed by the number (e.g. H8 12):")
            if input2 == 'Q':
                valid = True
            if input2 == "CLEAR":
                valid = True
            elif len(input2) < 4:
                valid = False
            else:
                col = input2[0]
                row = input2[1]
                num = input2[3:]
                if col >= 'H' or col <= 'A':
                    valid = False
                elif row >= '8' or row <= '1':
                    valid = False
                elif not num.isdigit():
                    valid = False
                elif int(num) >= 56 or int(num) <= 0:
                    valid = False
                elif int(num) not in remains and int(num) != 0:
                    valid = False
                elif not CheckSpace(origArr, col, row):
                    valid = False
                else:
                    valid = True
                # TODO: also give the user the ability to clear the board and clear a square (entering a square with a number already contained in it will clear it)
        print("valid input")
        if input2 == "CLEAR":
            arr = ClearBoard(origArr, arr)
        elif input2 != 'Q':
            # to clear a square, the user should enter the square followed by a 0
            arr, remains = UpdateBoard(arr, remains, col, row, num)
        # TODO: update the square here with the new number, or set it to 0
        if not CheckCompleted(arr):
            completed = False
        else:
            completed = True
    if completed:
        print("Congratulations, you solved the puzzle!")

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