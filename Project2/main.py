
# Main function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    # if sudoku is solved, return True
    if is_complete(board):
        return True

    # find the corresponding row and column of the empty cell
    row, col = find_empty_cell(board)
    # check if any number from 1 to 9 can be placed in that cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # goes to the next empty cell and check if any number can be placed there
            if solve_sudoku(board):
                return True

            # Reset the cell if the solution is not found
            board[row][col] = 0

    # return False if not any number can be placed
    return False


# function to check if sudoko is solved
def is_complete(board):
    for row in range(9):
        for col in range(9):
            # check condition fails if there exists any 0 in the sudoku
            if board[row][col] == 0:
                return False
    return True


# function to find empty cells in the sudoku and if there is any, returns the index
def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            # if there is any empty cell, return the index
            if board[row][col] == 0:
                return row, col
    return None, None


# function to check if any number in each index can could be possible
def is_valid(board, row, col, num):
    # Check if the number already exists in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number already exists in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number already exists in the 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    # check if any number in the 3x3 grid is equal to the number we are trying to place
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


# initializing sudoku for input
sudoku = []
for i in range(9):
    single_row = list(input().split())
    sudoku.append(single_row)

# convert each index to integer
for i in range(9):
    for j in range(9):
        sudoku[i][j] = int(sudoku[i][j])

# if sudoko can be solved, print the solution
if solve_sudoku(sudoku):
    for row in sudoku:
        for element in row:
            print(element, end=' ')
        print()
else:
    print("No solution found.")
