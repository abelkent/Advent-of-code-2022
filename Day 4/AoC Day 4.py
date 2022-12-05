"""
AoC Day 4
"""

def sol_a(filepath):
    
    #Imports and formats data
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
    
    #Overlaps initialised at zero
    overlaps = int(0)
    
    #Iterates through lines of data
    for line in data:
        #Splits each line into pairs
        pair_a = line.split(",")[0]
        pair_b = line.split(",")[1]
    
        #Splits each pair into start and end
        start_a = int(pair_a.split("-")[0])
        end_a = int(pair_a.split("-")[1])
        
        start_b = int(pair_b.split("-")[0])
        end_b = int(pair_b.split("-")[1])
        
        #Incremements overlaps if A is within B
        if ((start_a >= start_b) and (end_a <= end_b)):
            print("A within B")
            overlaps+=1
        
        #Increments overlaps if B is within A
        elif ((start_b >= start_a) and (end_b <= end_a)):
            print("B within A")
            overlaps+= 1
    
    #Returns overlaps
    return overlaps

""""test_a = sol_a("test.txt")
actual_a = sol_a("input.txt")"""
        
def sol_b(filepath):
    
    #Imports and formats data
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
    
    #Overlaps initialised at zero
    overlaps = int(0)
    
    #Iterates through lines of data
    for line in data:
        #Splits each line into pairs
        pair_a = line.split(",")[0]
        pair_b = line.split(",")[1]
    
        #Splits each pair into start and end
        start_a = int(pair_a.split("-")[0])
        end_a = int(pair_a.split("-")[1])
        
        start_b = int(pair_b.split("-")[0])
        end_b = int(pair_b.split("-")[1])
        
        #Local overlaps set to points present in both ranges
        local_overlaps = [point for point in range(start_a,end_a+1) if point in range(start_b,end_b+1)]
        
        #If lenght of local_overlaps is greater than zero, overlaps is incremented
        if len(local_overlaps) > 0:
            overlaps +=1
    
    #Overlaps is returned
    return overlaps

test_b = sol_b("test.txt")
actual_b = sol_b("input.txt")