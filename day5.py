# Day 5

def inRange(num, rangeNum):
    start, end = rangeNum
    if num >= start and num <= end:
        return True    
    return False

def isFresh(num, ranges):
    for rangeNum in ranges:
        if inRange(num, rangeNum):
            return True
    return False

def part1(numList, ranges):
    count = 0
    for num in numList:
        if isFresh(num, ranges):
            count += 1
    return count
def part2(ranges):
    ranges = sorted(ranges, key=lambda item: item[0])
    merged_ranges = []
    merged_ranges.append(ranges[0])
    for i in range(1, len(ranges)):
        start, end = ranges[i]
        if merged_ranges[-1][1] >= start:
            merged_ranges[-1] = (merged_ranges[-1][0], max(end, merged_ranges[-1][1]))
        else: 
            merged_ranges.append((start, end))
    count = 0
    for start, end in merged_ranges: 
        count += (end - start) + 1
    return count

def main():
    ranges = []
    while True:
        rangeNum = input()
        if rangeNum == "":
            break
        rangeNum = rangeNum.split("-")
        ranges.append((int(rangeNum[0]), int(rangeNum[1])))
    numList = []
    while True:
        num = input()
        if num == "":
            break
        numList.append(int(num))
    print(part1(numList, ranges))
    print(part2(ranges))


main()