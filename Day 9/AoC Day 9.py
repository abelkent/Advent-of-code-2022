"""
AoC Day 9
"""

import math

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
        data = [line.split() for line in data]
        
    #X,Y
    head_pos = [0,0]
    tail_pos = [1,1]
    print(math.dist(head_pos, tail_pos))
    
    
    visited_points= list()
    
    #print(math.dist(head_pos, tail_pos))
    
    def head_move(direction, scale):
        
        for index in range(int(scale)):
            if direction == "L":
                head_pos[0] -= 1
            elif direction == "R":
                head_pos[0] += 1
            elif direction == "D":
                head_pos[1] -= 1
            elif direction == "U":
                head_pos[1] += 1
            
            tail_move()
            print(head_pos, tail_pos)
            
        print("EOL")
        print(len(visited_points))
        
    def tail_move():
        distance = math.dist(head_pos, tail_pos)
        if distance <= 1.5:
            pass
        else:
            if head_pos[0] != tail_pos[0]:
                if head_pos[0] > tail_pos[0]:
                    tail_pos[0] += 1
                else:
                    tail_pos[0] -= 1
            
            if head_pos[1] != tail_pos[1]:
                if head_pos[1] > tail_pos[1]:
                    tail_pos[1] += 1
                else:
                    tail_pos[1] -= 1
    
        if tail_pos not in visited_points:
            visited_points.append(list(tail_pos))
    
    
    for line in data:
        head_move(line[0], line[1])
    
    print(len(visited_points))
        
        
        