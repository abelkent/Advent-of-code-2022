"""
AoC 2022 Day 1
"""

def sol_a(filepath):
    
    #Reads data as array and strips "\n" from each line
    with open(filepath) as file:
        data = file.readlines()
        data = [x.strip("\n") for x in data]
    
    #Defines array of totals and integer of "local_total"
    totals = list()
    local_total = int(0)
    
    #Iterates through each line in input
    for line in data:
        #Adds each entry to local total
        if len(line) > 0:
            local_total += int(line)
        
        #When a break is reached, local_total is appended to totals
        else:
            totals.append(local_total)
            local_total = 0
    
    #local_total is added to total for final value
    totals.append(local_total)
    
    #Maximum value is returned from totals
    return max(totals)

"""test_a = sol_a("test.txt")
actual_a = sol_a("input.txt")"""

def sol_b(filepath):
    
    #Reads data as array and strips "\n" from each line
    with open(filepath) as file:
        data = file.readlines()
        data = [x.strip("\n") for x in data]
    
    #Defines array of totals and integer of "local_total"
    totals = list()
    local_total = int(0)
    
    #Iterates through each line in input
    for line in data:
        #Adds each entry to local total
        if len(line) > 0:
            local_total += int(line)
        #When a break is reached, local_total is appended to totals
        else:
            totals.append(local_total)
            local_total = 0

    #local_total is added to total for final value
    totals.append(local_total)
    
    #totals is sorted from smallest to largest
    totals.sort()
    
    #top_3 is defined as the sum of the last (largest) 3 elements in the array
    top_3= sum(totals[-3:])
    #top_3 is returned
    return(top_3)

"""test_b = sol_b("test.txt")
actual_b= sol_b("input.txt")"""