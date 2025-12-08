# Day 1 

def findPassword(puzzle):
    pos = 50
    password = 0 
    for direction, step in puzzle:  
        # full = step // 100
        # move = step % 100
        # if direction == "L":
        #     new_pos = (pos - move) % 100
        #     partial = 1 if new_pos > pos else 0
        # else:  # "R"
        #     new_pos = (pos + move) % 100
        #     partial = 1 if new_pos < pos else 0
        # print(new_pos)
        # pos = new_pos
        # password += full + partial
        for _ in range(step):
            if direction == "L":
                pos = (pos - 1) % 100
            else:
                pos = (pos + 1) % 100
                
            if pos == 0:
                password += 1
    return password

def main():
    puzzle = []
    while True: 
        instruction = input()
        if instruction == "-1": 
            break
        puzzle.append((instruction[0], int(instruction[1:])))
    password = findPassword(puzzle)
    print("The password is: ", password)
    return



if __name__ == "__main__":
    main()
    
