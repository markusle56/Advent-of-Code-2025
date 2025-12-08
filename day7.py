#Day 7
def getSplitterIndex(row):
    splitter = []
    for i in range(len(row)):
        if row[i] == "^":
            splitter.append(i)
    return splitter

def getCurrentBeam(splitter, beam):
    new_beam = []
    count = 0
    def addSplittedBeam(idx):
        if idx - 1 not in new_beam:
            new_beam.append(idx-1)
        if idx + 1 not in new_beam:
            new_beam.append(idx + 1) 
    for i in beam:
        if i in splitter:
            addSplittedBeam(i)
            count += 1
        else:
            if i not in new_beam:
                new_beam.append(i)
    return new_beam, count
            
def part1(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    beam = []
    total_split = 0
    for j in range(m):
        if puzzle[0][j] == "S":
            beam.append(j)
    for i in range(1,n):
        splitter = getSplitterIndex(puzzle[i])
        beam, count = getCurrentBeam(splitter, beam)
        total_split += count
    return total_split
memo = {}
def travel(splitter_layers, beam_idx, level):
    if len(splitter_layers) <= level:
        return 1

    if (beam_idx, level) in memo.keys():
        return memo[(beam_idx, level)]
    
    if beam_idx in splitter_layers[level]:
        timelines = travel(splitter_layers, beam_idx - 1, level + 1) + travel(splitter_layers, beam_idx + 1, level + 1)
    else:
        timelines = travel(splitter_layers, beam_idx, level + 1)
    
    memo[(beam_idx, level)] = timelines
    return timelines
def part2(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    memo = {}
    splitter_layers = []
    for j in range(m):
        if puzzle[0][j] == "S":
            beam = j
    for i in range(1,n): 
        splitter_layers.append(getSplitterIndex(puzzle[i]))
    return travel(splitter_layers, beam, 0)
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