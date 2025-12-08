# Day 8 
import math

def calDistance(box1, box2):
    x1,y1,z1 = box1
    x2,y2,z2 = box2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def calculate_all_pairs(boxes):
    n = len(boxes)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = calDistance(boxes[i], boxes[j])
            pairs.append((distance, i, j))
    return sorted(pairs)

parent = {}
rank = {}

def find(i):
    if parent[i] == i:
        return i
    else:
        return find(parent[i])

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        rank[px] += rank[py]
        parent[py] = px
        return True
    else:
        return False
def part1(boxes, times):
    n = len(boxes) 
    for i in range(n):
        parent[i] = i
        rank[i] = 1
    pairs = calculate_all_pairs(boxes)
    for i in range(times):
        _, b1, b2 = pairs[i]
        union(b1,b2)
    juntions = []
    for key, value in parent.items():
        if key == value:
            juntions.append(rank[key])
    juntions = sorted(juntions, reverse = True)
    print(juntions)
    return juntions[0] * juntions[1] * juntions[2]

def part2(boxes):
    n = len(boxes) 
    answer = 0
    for i in range(n):
        parent[i] = i
        rank[i] = 1
    pairs = calculate_all_pairs(boxes)
    for i in range(len(pairs)):
        _, b1, b2 = pairs[i]
        if union(b1,b2):
            answer = boxes[b1][0] * boxes[b2][0]
    return answer
def main():
    puzzle = []
    while True:
        row = input()
        if row == "":
            break
        puzzle.append([int(s) for s in row.split(",")])
    print(part1(puzzle, 1000))
    print(part2(puzzle))
main()