"""
AoC Day 5
"""

def sol_a(stacks_filepath, instructions_filepath):
    
    #Data importing and processing
    #I seperated instructions and stacks into separate files prior to this
    with open(stacks_filepath) as stacks_file:
        stacks = stacks_file.readlines()
        stacks = [line.strip("\n") for line in stacks]
        
    with open(instructions_filepath) as instructions_file:
        instructions = instructions_file.readlines()
        instructions = [line.strip("\n") for line in instructions]
    
    #Stack initialisation
    stacks_all = list()
    for gap in range(1, len(stacks[0]), 4):
        stacks_all.append([])
    


    #Stack population
    for line in stacks:

        for index in range(1, len(line),4):
            if index == 1:
                stack_index = 0
            else:
                stack_index = int((index-1)/4)
            
            retrieved_stack = stacks_all[stack_index]
            retrieved_stack.insert(0, line[index])
            stacks_all[stack_index] = retrieved_stack
    
    #Stack formatting
    for stack in stacks_all:
        stack.pop(0)
        while " " in stack:
            stack.remove(" ")
    
    
    #Instruction initialisation
    instructions_all = list()
    
    
    #Instruction population
    for line in instructions:
        local_instruction = list()
        line = line.split(" ")
        
        for item in line:
            try:
                int(item)
            except:
                line.remove(item)
            else:
                item = int(item)
        
        line = [int(x) for x in line]
        instructions_all.append(line)
    
    
    #Instructions processing
    for instruction in instructions_all:
        quantity = instruction[0]
        source = instruction[1]-1
        target = instruction[2]-1
        print(quantity, source, target)
        
        for repeat in range(quantity):
            source_stack = stacks_all[source]
            target_stack = stacks_all[target]
            
            moved = source_stack.pop()
            target_stack.append(moved)
            
            stacks_all[source] = source_stack
            stacks_all[target] = target_stack

    
    #Final answer generation
    output = list()
    for stack in stacks_all:
        output.append(stack[-1])
        
    return("".join(output))
                
                
test = sol_a("test stacks.txt","test instructions.txt")
actual_a = sol_a("input stacks.txt","input instructions.txt")