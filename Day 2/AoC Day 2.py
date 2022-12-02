"""
AoC Day 2
"""

"""
Opponent:
    A = Rock
    B = Paper
    C = Scissors

Me:
    X = Rock
    Y = Paper
    Z = Scissors
    

Points:
    Rock = 1
    Paper = 2
    Scissors = 3
    
    Loss = 0
    Draw = 3
    Win = 6
"""


def sol_a(filepath):
    #Imports data and reformats it to a 2 character string
    with open(filepath) as file:
        data = file.readlines()
        data = [x.strip("\n") for x in data]
        data = [x.replace(" ","") for x in data]
    
    #Score initialised as zero
    score = int(0)
    
    #Lists of winning and drawing (and losing) move combinations are initialised
    winning_rounds = ["AY", "BZ","CX"]
    drawing_rounds = ["AX","BY","CZ"]
    #losing_rounds = ["AZ", "BX", "CY"]
    
    #Dictionary containing scores for the player's moves is initialised
    player_score = {"X":1, "Y":2, "Z":3}
    
    #Iterates through entries and increments score as needed
    for line in data:
        player = line[1]
        
        if line in winning_rounds:
            score+= 6
        elif line in drawing_rounds:
            score+= 3
        
        score+= player_score.get(player)
    
    #score is returned
    return score

"""
test_a = sol_a("test.txt")
actual_a = sol_a("input.txt")
"""


"""
X = Lose (0)
Y = Draw (3)
Z = Win (6)
"""

def sol_b(filepath):
    #Imports data and reformats it to a 2 character string
    with open(filepath) as file:
        data = file.readlines()
        data = [x.strip("\n") for x in data]
        data = [x.replace(" ","") for x in data]
        
    #Score initialised as zero
    score = int(0)

    #Dictionaries with the scores the player's should be incremented with depending
    #on round outcome and move made are initialised
    win_dict = {"A":2, "B":3, "C":1}
    draw_dict = {"A": 1, "B": 2, "C":3}
    lose_dict = {"A":3,"B":1, "C":2}
    

    #Dictionary with the scores the players will be incremented with depending 
    #on round outcome is initialised
    player_score_dict = {"X":0, "Y":3, "Z":6}


    #Iterates through entries and increments score as needed
    for line in data:
        opponent = line[0]
        player = line[1]
        
        score += player_score_dict.get(player)
        
        if player == "X":
            score += lose_dict.get(opponent)
        elif player == "Y":
            score += draw_dict.get(opponent)
        elif player == "Z":
            score += win_dict.get(opponent)
    
    #score is returned
    return score
    
"""test_b = sol_b("test.txt")
actual_b = sol_b("input.txt")"""
