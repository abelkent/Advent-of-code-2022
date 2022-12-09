"""
AoC Day 8
"""

def sol_a(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
        data = [[int(x) for x in line] for line in data]
    
    x_max = len(data[0])
    y_max = len(data)
    
    
    def check_left(y_pos,x_pos):
        value = data[y_pos][x_pos]
        left_range = []
        for x_point in range(x_pos-1,-1,-1):
            left_range.append(data[y_pos][x_point])
        
        for item in left_range:
            if item >= value:
                return False
        
        return True
        
                        
    def check_right(y_pos,x_pos):
        value = data[y_pos][x_pos]
        right_range = []
        for x_point in range(x_pos+1,len(data[0]),1):
            right_range.append(data[y_pos][x_point])
        
        for item in right_range:
            if item >= value:
                return False
        
        return True
        

    def check_up(y_pos,x_pos):
        value = data[y_pos][x_pos]
        up_range = []
        for y_point in range(y_pos-1,-1,-1):
            up_range.append(data[y_point][x_pos])
        
        print(up_range)
        
        for item in up_range:
            if item >= value:
                return False
            
        return True

        
    def check_down(y_pos,x_pos):
        value = data[y_pos][x_pos]
        down_range = []
        for y_point in range(y_pos+1,len(data),1):
            down_range.append(data[y_point][x_pos])
        
        for item in down_range:
            if item >= value:
                return False
            
        return True
        
    
    def visibility_check(y_pos,x_pos):
        visible_axes = []
        visible_axes.append(check_left(y_pos, x_pos))
        visible_axes.append(check_right(y_pos,x_pos))
        visible_axes.append(check_up(y_pos,x_pos))
        visible_axes.append(check_down(y_pos,x_pos))
        
        if True in visible_axes:
            return True
        else:
            return False
    
    total = int(0)
    
    
    for y_index in range(len(data)):
        for x_index in range(len(data[0])):
            print(y_index, x_index)
            if visibility_check(y_index, x_index) == True:
                total += 1
            print(total)
                
    print(total)




"""test = sol_a("test.txt")
actual = sol_a("input.txt")"""


def sol_b(filepath):
    
    with open(filepath) as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]
        data = [[int(x) for x in line] for line in data]
    
    x_max = len(data[0])
    y_max = len(data)
    
    
    def check_left(y_pos,x_pos):
        value = data[y_pos][x_pos]
        
        score = int(0)     
        
        for x_point in range(x_pos-1,-1,-1):
            score += 1
            tree_height = data[y_pos][x_point]
            if tree_height >= value:
                break
        
        return score
                        
    def check_right(y_pos,x_pos):
        value = data[y_pos][x_pos]
        
        score = int(0)     
        
        for x_point in range(x_pos+1,len(data[0]),1):
            score += 1
            tree_height = data[y_pos][x_point]
            if tree_height >= value:
                break
        
        return score

    def check_up(y_pos,x_pos):
        value = data[y_pos][x_pos]
        
        score = int(0)     
        
        for y_point in range(y_pos-1,-1,-1):
            score += 1
            tree_height = data[y_point][x_pos]
            if tree_height >= value:
                break
        
        return score

        
    def check_down(y_pos,x_pos):
        value = data[y_pos][x_pos]
        
        score = int(0)     
        
        for y_point in range(y_pos+1,len(data),1):
            score += 1
            tree_height = data[y_point][x_pos]
            if tree_height >= value:
                break
        
        return score
    
    def scenic_calc(y_pos, x_pos):
        score = 1
        score *= check_left(y_pos,x_pos)
        score *= check_right(y_pos,x_pos)
        score *= check_up(y_pos,x_pos)
        score *= check_down(y_pos,x_pos)

        return score
        
        
    
    total = int(0)
    
    
    for y_index in range(len(data)):
        for x_index in range(len(data[0])):
            if scenic_calc(y_index,x_index) > total:
                total = scenic_calc(y_index, x_index)
    
    return total
                
test = sol_b("test.txt")
actual = sol_b("input.txt")