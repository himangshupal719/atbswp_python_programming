def pictureGrid(grid):
    for y in range(6):
        print('')
        for x in range(9):
            print(grid[x][y], end='')


# x = inner lists
# y = elements in each list
# while pointer is in first element (y = 0) of the first list (x =0) , print the first element of the 1st list (grid[0][0]).
# while the pointer is in first element (y = 0) of the 2nd list (x = 1), print the first element of the 2nd list (grid[0][1]).
# while the pointer is in first element (y = 0) of the 3rd list (x = 2), print the first element of the 3rd list (grid[0][2]).
# while the pointer is in first element (y = 0) of the 4th list (x = 3), print the first element of the 4th list (grid[0][3]).
# and so on. 

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

pictureGrid(grid)
