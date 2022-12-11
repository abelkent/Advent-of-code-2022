"""
AoC Day 11
"""

import math

monkeys = list()

import time

class Monkey_Old():
    def __init__(self, operator, change, test, true_target, false_target, inspections = int(0), objects = list()):
        self.objects = objects
        self.operator = operator
        self.change = change
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.inspections = inspections
        
    def action(self):
        
        if self.objects == []:
            pass
        
        else:
            worry = self.objects[0]
            change = self.change
            
            if self.change == "old":
                change = int(worry)
            
            if self.operator == "+":
                worry += change
            elif self.operator == "-":
                worry -= change
            elif self.operator == "*":
                worry *= change
                
            worry = math.floor(worry / 3)
            
            
            if (worry % self.test) == 0:
                monkeys[self.true_target].recieve(worry)
                #print(str(worry) +" passed to "+str(self.true_target))
            else:
                monkeys[self.false_target].recieve(worry)
                #print(str(worry) +" passed to "+str(self.false_target))

        self.inspections += 1
        self.objects.pop(0)
                
    def recieve(self,item):
        self.objects.append(item)
        
    def output(self):
        print(self.objects)
        

class Monkey():
    def __init__(self, operator, change, test, true_target, false_target, inspections = int(0), objects = list()):
        self.objects = objects
        self.operator = operator
        self.change = change
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.inspections = inspections
    

        
    def action(self):
        
        def get_divisors(integer):
            output = list()
            for i in range(1,integer+1):
                if (integer % i) == 0:
                    output.append(i)
            
            return output
        
        def lcm(lst):
            lcm_temp = max(lst)
            while True:
                if all(lcm_temp % x == 0 for x in lst):
                    break
                lcm_temp = lcm_temp + 1
            return lcm_temp
        
        if self.objects == []:
            pass
        
        else:
            worry = self.objects[0]
            change = self.change
            
            if self.change == "old":
                change = int(worry)
            
            if self.operator == "+":
                worry += change
            elif self.operator == "-":
                worry -= change
            elif self.operator == "*":
                worry *= change
                
                
                            
            if (worry % self.test) == 0:
                monkeys[self.true_target].recieve(worry%lcm(get_divisors(worry)+[self.test]))
                print(str(worry) +" passed to "+str(self.true_target))
            else:
                monkeys[self.false_target].recieve(worry%lcm(get_divisors(worry)+[self.test]))
                print(str(worry) +" passed to "+str(self.false_target))

        self.inspections += 1
        self.objects.pop(0)
                
    def recieve(self,item):
        self.objects.append(item)
        
    def output(self):
        print(self.objects)
        

def sol_b_test():
    monkeys.append(Monkey(objects = [79,98], 
                          operator = "*",
                          change = 19,
                          test = 23,
                          true_target = 2,
                          false_target = 3))

    monkeys.append(Monkey(objects = [54, 65, 75, 74],
                          operator = "+",
                          change = 6,
                          test = 19,
                          true_target = 2,
                          false_target = 0))

    monkeys.append(Monkey(objects = [79, 60, 97],
                          operator = "*",
                          change = "old",
                          test = 13,
                          true_target = 1,
                          false_target = 3))
    
    monkeys.append(Monkey(objects = [74],
                          operator = "+",
                          change = 3,
                          test = 17,
                          true_target = 0,
                          false_target = 1))



                
    
    def take_round():
        for monkey in monkeys:
            for index in range(len(monkey.objects)):
                monkey.action()
                #time.sleep(2)
            print("---")
        
        for monkey in monkeys:
            monkey.output()
    
        print("----------------- END OF ROUND -----------------")
    
    for index in range(20):
        take_round()
    
    total_inspections = list()
    
    for monkey in monkeys:
        total_inspections.append(monkey.inspections)
    
    print(total_inspections)
    
sol_b_test()

monkeys = list()

def sol_a_actual():
    
    #Monkey 0
    monkeys.append(Monkey(objects = [71, 86],
                          operator = "*",
                          change = 13,
                          test = 19,
                          true_target = 6,
                          false_target = 7))
    #Monkey 1
    monkeys.append(Monkey(objects = [66, 50, 90, 53, 88, 85],
                          operator = "+",
                          change = 3,
                          test = 2,
                          true_target = 5,
                          false_target = 4))
    #Monkey 2
    monkeys.append(Monkey(objects = [97, 54, 89, 62, 84, 80, 63],
                          operator = "+",
                          change = 6,
                          test = 13,
                          true_target = 4,
                          false_target = 1))
    #Monkey 3
    monkeys.append(Monkey(objects = [82, 97, 56, 92],
                          operator = "+",
                          change = 2,
                          test = 5,
                          true_target = 6,
                          false_target = 0))
    #Monkey 4
    monkeys.append(Monkey(objects = [50, 99, 67, 61, 86],
                          operator = "*",
                          change = "old",
                          test = 7,
                          true_target = 5,
                          false_target = 3))
    #Monkey 5
    monkeys.append(Monkey(objects = [61, 66, 72, 55, 64, 53, 72, 63],
                          operator = "+",
                          change = 4,
                          test = 11,
                          true_target = 3,
                          false_target = 0))
    #Monkey 6
    monkeys.append(Monkey(objects = [59, 79, 63],
                          operator = "*",
                          change = 7,
                          test = 17,
                          true_target = 2,
                          false_target = 7))
    #Monkey 7
    monkeys.append(Monkey(objects = [55],
                          operator = "+",
                          change = 7,
                          test = 3,
                          true_target = 2,
                          false_target = 1))
    def take_round():
        for monkey in monkeys:
            for index in range(len(monkey.objects)):
                monkey.action()
                #time.sleep(2)
            print("---")
        
        for monkey in monkeys:
            monkey.output()
    
        print("----------------- END OF ROUND -----------------")
    
    for index in range(20):
        take_round()
    
    total_inspections = list()
    
    for monkey in monkeys:
        total_inspections.append(monkey.inspections)
    
    print(total_inspections)


