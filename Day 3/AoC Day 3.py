"""
AoC Day 3
"""

import string

def sol_a(filepath):
    
    #Creates point_dict with points value associated with each character
    points_dict = dict(zip(string.ascii_lowercase, range(1,27)))
    points_dict.update(zip(string.ascii_uppercase, range(27, 53)))

    #Total priority initialised
    total_priority = int(0)

    #Data imported and formatted
    with open(filepath) as file:
        data = file.readlines()
        data = [x.strip("\n") for x in data]
        
    
    #Iterates through lines of data
    for line in data:
        #For each line, it is split into 2 "pockets"
        divisor = int(len(line)/2)
        pocket_a = line[divisor:]
        pocket_b = line[:divisor]
        
        #Overlap between each pockets is identified
        overlap = [x for x in pocket_a if x in pocket_b][0]
        
        #Total priority is incremented by appropriate points
        total_priority += points_dict.get(overlap)
    
    #Total priority returned
    return(total_priority)

"""test_a = sol_a("test.txt")
actual_b = sol_a("input.txt")"""


def sol_b(filepath):

    #Creates point_dict with points value associated with each character
    points_dict = dict(zip(string.ascii_lowercase, range(1,27)))
    points_dict.update(zip(string.ascii_uppercase, range(27, 53)))

    #Total priority initialised
    total_priority = int(0)

    #Data imported and formatted
    with open(filepath) as file:
        data = file.readlines()
        data = [x.strip("\n") for x in data]
    
    
    #Cache memory initialised
    cache = list()
    
    #Iterates through chunks of data in groups of 3 and adds them to the cache
    for index in range(0, len(data),3):
        cache.append(data[index])
        cache.append(data[index+1])
        cache.append(data[index+2])

        #Overlap is identified
        overlap = [x for x in cache[0] if ((x in cache[1]) and (x in cache[2]))][0]
        
        #Total priority incremented
        total_priority += points_dict.get(overlap)
        
        #Cache reset
        cache = list()
    
    #Total priority returned
    return(total_priority)
        

test_b = sol_b("test.txt")
actual_b = sol_b("input.txt")
