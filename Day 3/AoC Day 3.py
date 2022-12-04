"""
AoC Day 3
"""

import string

def sol_a(filepath):
    
    points_dict = dict(zip(string.ascii_lowercase, range(1,27)))
    points_dict.update(zip(string.ascii_uppercase, range(27, 53)))

    total_priority = int(0)

    with open(filepath) as file:
        data = file.readlines()
        data = [x.strip("\n") for x in data]
        
    for line in data:
        divisor = int(len(line)/2)
        pocket_a = line[divisor:]
        pocket_b = line[:divisor]
        
        overlap = [x for x in pocket_a if x in pocket_b][0]
        
        total_priority += points_dict.get(overlap)
    
    return(total_priority)

"""test = sol_a("test.txt")
actual = sol_a("input.txt")"""

def sol_b(filepath):

    points_dict = dict(zip(string.ascii_lowercase, range(1,27)))
    points_dict.update(zip(string.ascii_uppercase, range(27, 53)))

    total_priority = int(0)

    with open(filepath) as file:
        data = file.readlines()
        data = [x.strip("\n") for x in data]
    
    
    
    cache = list()
    for index in range(0, len(data),3):
        cache.append(data[index])
        cache.append(data[index+1])
        cache.append(data[index+2])

        overlap = [x for x in cache[0] if ((x in cache[1]) and (x in cache[2]))][0]
        total_priority += points_dict.get(overlap)
        cache = list()
    
    return(total_priority)
        

test_b = sol_b("test.txt")
actual_b = sol_b("input.txt")
