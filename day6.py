#day 6
 
def multiply(row):
    product = 1
    for i in row:
        product *= int(i)
    return product
def sum_row(row):
    total = 0 
    for i in row: 
        total += int(i)
    return total 

def rotate(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    new_puzzle = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(puzzle[j][i])
        new_puzzle.append(row)
            
    return new_puzzle
            
def part1(puzzle):
    total = 0
    
    instruction = puzzle[-1]
    puzzle = rotate(puzzle[:-1])

    for i in range(len(instruction)):
        if instruction[i] == "+":
            total += sum_row(puzzle[i])
        else:
            total += multiply(puzzle[i])
    
#DAYDaydfasdfdssdsdffdsfsd    return total

def isEmptyCol(grid, i):
    for j in range(len(grid)):
        if grid[j][i] != " ":
            return False
    return True


def colNum2RowNum(grid):
    row = []
    new_grid = []
    n = len(grid)
    m = len(grid[0])
    for i in range(m):
        if isEmptyCol(grid, i):
            new_grid.append(row)
            row = []
        else:
            num = ""
            for j in range(n):
                if grid[j][i] != " ":
                    num += grid[j][i]
            row.append(num)
    new_grid.append(row)
    return new_grid

def part2(puzzle):
    instruction = puzzle[-1].split()
    puzzle = colNum2RowNum(puzzle[:-1])
    total = 0
    for i in range(len(instruction)):
        if instruction[i] == "+":
            total += sum_row(puzzle[i])
        else:
            total += multiply(puzzle[i])
    
    return total
    return 
    
def main():
    puzzle = []
    part2_puzzle = []
    while True:
        row = input()
        if row == "":
            break
        part2_puzzle.append(row)
        row = row.split()
        puzzle.append(row)
    print(part1(puzzle))
    print(part2(part2_puzzle))
main()
