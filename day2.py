# Day 2 

def isPattern(num):
    for i in range(1, len(num)//2 + 1):
        pattern = num[:i]
        num_left = num[i:]
        while len(num_left) >= i:
            if pattern == num_left[:i]:
                num_left = num_left[i:]
            else:
                break
        if not len(num_left):
            return True
    return False

def isRepeatTwice(num):
    n = len(num)//2
    if len(num) < n:
        return False
    if num[:n] == num[n:]:
        return True
    else:
        return False

def part1(puzzle):
    accomulation = 0 
    for start, end in  puzzle:
        for i in range(start, end + 1):
            if isRepeatTwice(str(i)):
                accomulation += i 
    return accomulation

def part2(puzzle):
    accomulation = 0 
    for start, end in  puzzle:
        for i in range(start, end + 1):
            if isPattern(str(i)):
                accomulation += i 
    return accomulation

def main():
    ranges = input("Enter range of product IDs:")
    ranges = ranges.split(",")
    puzzle = []
    for product_range in ranges:
        product_range = product_range.split('-')
        puzzle.append((int(product_range[0]), int(product_range[1])))
    print(part1(puzzle))
    print(part2(puzzle))

    return 

if __name__ == "__main__":
    main()