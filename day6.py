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
    
    return total 

def main():
    puzzle = []
    while True:
        row = input()
        if row == "":
            break
        row = row.split()
        puzzle.append(row)
    print(part1(puzzle))
main()
