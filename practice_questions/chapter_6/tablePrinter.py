'''
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Expected Output: 

  apple Alice  dogs
 orange  Bob cats
cherris Carlol moose
 banana  David goose

'''


def printTable(tableData):

    numRow = len(tableData)
    numCol = len(tableData[0])

    colWidth = [0]*len(tableData)

    for row in range(numRow):
        maxWidth = 0
        for col in range(numCol):
            if len(tableData[row][col]) > maxWidth:
                maxWidth = len(tableData[row][col])
        colWidth[row] = maxWidth
    
    print(f'colWidth:{colWidth},  numCol:{numCol}, numRow:{numRow}')
    
    for col in range(4):
         print('')
         for row in range(3):
             print(tableData[row][col].rjust(colWidth[row]), end = ' ')


tableData = [['apple', 'oranges', 'cherris','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]
printTable(tableData)



