#!/usr/bin/env python3

path = r"/home/vuhl/Projects/AoC2022/Day1/data.txt"

with open(path) as d:
    data = [line.rstrip('\n') for line in d]
    
weights = []
current_weight = 0

for d in data:
    if d != "":
        d = int(d)
        current_weight += d
        
    else:
        weights.append(current_weight)
        current_weight = 0
        
#Solution for problem 1:
print(max(weights))

#Solution for problem 2:
weights.sort(reverse=True)
top_3 = weights[:3]
print(sum(top_3))