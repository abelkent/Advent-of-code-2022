"""
AoC Day 12
"""

import string

def sol_a(filepath):
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
        data = [[x for x in line] for line in data]
    

    
    letters = string.ascii_lowercase
    numbers = range(1,27)
    
    height_dict = dict(zip(letters,numbers))
        
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] in height_dict.keys():
                data[row][col] = height_dict.get(data[row][col])
    
    
    def get_all_neighbours(col,row):
        
        #Top, Bottom, Left, Right
        neighbours = []
        
        #Top
        if col != 0:
            neighbours.append([col-1,row])
        
        #Bottom
        if col != len(data)-1:
            neighbours.append([col+1,row])
        
        #Left
        if row != 0:
            neighbours.append([col, row-1])
        
        #Right
        if row != len(data[0])-1:
            neighbours.append([col, row+1])
            
        
        return neighbours
            
    
    def get_valid_neighbours(height,coords):
        output = []
        for entry in coords:
            col = entry[0]
            row = entry[1]
            
            if data[col][row] >= height + 1:
                output.append(entry)
        
        return output
        
    
    
sol_a("test.txt")