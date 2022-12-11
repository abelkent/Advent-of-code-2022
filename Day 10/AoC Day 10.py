"""
AoC Day 10
"""
def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
        data = [line.split() for line in data]
    
    
    register = int(1)
    clock = int(1)
    outputs = list()
    
    chosen_ticks = [20,60,100,140,180,220]
    
    def clock_check():
        if clock in chosen_ticks:
            outputs.append(clock * register)
            print(clock, register, outputs)
    
    for entry in data:
        if len(entry) == 1:
            clock += 1
            clock_check()
        
        else:
            clock += 1
            clock_check()
            register += int(entry[1])
            clock += 1
            clock_check()

    
    return sum(outputs)

"""test = sol_a("test.txt")
actual = sol_a("input.txt")"""

def sol_b(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
        data = [line.split() for line in data]
    
    
    register = int(1)
    clock = int(1)
    
    output_lines = list()
    local_line = str()
    
    def line_clear():
        nonlocal local_line
        if len(local_line) == 20:
            output_lines.append(local_line)
            local_line = str()
    
            
    
    for entry in data:
        if len(entry) == 1:
            clock += 1
            clock_check()
        
        else:
            clock += 1
            clock_check()
            register += int(entry[1])
            clock += 1
            clock_check()

    
    return sum(outputs)