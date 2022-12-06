"""
AoC Day 6
"""

def sol_a(filepath):
    
    #Import data
    with open(filepath) as file:
        data = file.read()
    
    #Initialise cache and index
    cache = [None, None, None, None]
    index = 0
    
    #Iterates through characters in data
    for character in data:
        cache.append(character)
        cache.pop(0)
        index+=1
        
        #If conditions are satisfied, return index
        if (len(set(cache)) == 4) and (None not in cache):
            #print(cache)
            return index

"""test_a = sol_a("test.txt")
actual_a = sol_a("input.txt")"""

def sol_b(filepath):
    
    #Import data
    with open(filepath) as file:
        data = file.read()

    #Initialise cache and index
    cache = [None, None, None, None, None, None, None,
             None, None, None, None, None, None, None]
    index = 0
    
    #Iterates through characters in data
    for character in data:
        cache.append(character)
        cache.pop(0)
        index+=1

        #If conditions are satisfied, return index
        if (len(set(cache)) == 14) and (None not in cache):
            #print(cache)
            return index

"""test_b = sol_b("test.txt")
actual_b = sol_b("input.txt")"""