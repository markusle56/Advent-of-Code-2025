# Day 3

def find_max(num: str):
    max_digit = int(num[0])
    max_position = 0 
    for i in range(1, len(num)):
        if max_digit < int(num[i]):
            max_digit = int(num[i])
            max_position = i 
    return max_digit, max_position
def calculate_jolts(num : str):
    firstB, positionB = find_max(num[: -1])
    secondB, _ = find_max(num[positionB + 1:])
    return firstB * 10 + secondB

def part1(puzzle):
    total = 0 
    for battery in puzzle:
        total += calculate_jolts(battery)
    return total 

def remove_min(battery):
    max_value = int(battery[1:])
    for i in range(1, len(battery)):
        val = int(battery[:i] + battery[i+1:])
        if max_value < val:
            max_value = val
    return str(max_value)
def calculate_jolts_12(battery):
    while len(battery) > 12:
        battery = remove_min(battery)
    return int(battery)
def part2(puzzle):
    total = 0 
    for battery in puzzle:
        total += calculate_jolts_12(battery)
    return total 

def main():
    puzzle = []
    while True:
        battery = input()
        if battery == "":
            break
        puzzle.append(battery)
    print(part1(puzzle))
    print(part2(puzzle))
    return 

if __name__ == "__main__":
    main()