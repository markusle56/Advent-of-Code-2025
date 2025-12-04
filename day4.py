def isAccessable(i, j, grid):
    step = [-1,0,1]
    count = 0
    for h in step:
        for v in step:
            if i + h >= len(grid) or i + h < 0: 
                continue
            elif j + v >= len(grid[0]) or j + v < 0:
                continue
            if grid[i+h][v + j] == "@":
                count += 1
    if count <= 4:
        return True
    else:
        return False

def part1(grid):
    n = len(grid)
    m = len(grid[0])
    count =0 
    for i in range(n): 
        for j in range(m): 
            if grid[i][j] == "@" and isAccessable(i,j,grid): 
                count +=1
    return count

def part2(grid):
    total = 0 
    count =0 
    n = len(grid)
    m = len(grid[0])
    new_grid = grid
    while True:

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@" and isAccessable(i,j, grid):
                    count += 1
                    new_grid[i]= grid[i][:j] + "x" + grid[i][j + 1:]
        if count == 0:
            break
        total += count 
        count = 0
        grid = new_grid
    return(total)
    
def main(): 
    puzzle = []
    while True:
        row = input()
        if row == "":
            break
        puzzle.append(row)
    print(part1(puzzle))
    print(part2(puzzle))
main()