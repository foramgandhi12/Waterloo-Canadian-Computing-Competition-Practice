# CCC 2019 Problem J5: Rule of Three
# Programmer: Foram Gandhi


rules = []

for count in range(1, 4):
    line = input().split()
    rules.append([line[0], line[1], count])

num_steps, start, goal = input().split()
num_steps = int(num_steps)
visited = set()

def solve(steps_left, seq, prev):

    if steps_left == 0 and seq == goal:
        return prev
    
    elif steps_left == 0:
        return False
    
    curr = (seq, steps_left)
    if curr in visited:
        return False
    else:
        visited.add(curr)
    
    
    for rule, sub, rule_num in rules:
        positions = find_index(seq, rule)
        
        for i in positions:
            new_seq = seq[:i] + sub + seq[i + len(rule):]      
            prev1 = prev.copy()
            prev1.append([rule_num, i + 1, new_seq])
            outcome = solve(steps_left - 1, new_seq, prev1)
            
            if outcome:
                return outcome
        
    
def find_index(seq, find_rule):
    indices_list = []
    curr_index = 0

    while True:
        curr_index = seq.find(find_rule, curr_index)
        if curr_index == -1:
            return indices_list
        else:
            indices_list.append(curr_index)
    
        curr_index += 1
        
ans = solve(num_steps, start, [])

for step in ans:
    print(step[0], step[1], step[2])
