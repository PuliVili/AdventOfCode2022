#!/usr/bin/env python3

path = r"/home/vuhl/Projects/AoC2022/Day3/data.txt"
with open(path) as d:
    data = [line.rstrip('\n') for line in d]

priorities = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sums = []

for row in data:
    s = 0
    common_chars = []
    first_i, second_i = row[:len(row)//2], row[len(row)//2:]
    for char in first_i:
        if char in second_i and not char in common_chars:
            common_chars.append(char)
            s += priorities.index(char)
        
    sums.append(s)
    
#print(sum(sums))

sums = []

for i in range(0,len(data), 3):
    print(data[i])
    s = 0
    common_chars = []
    batches = [] 
    
    batches.append(data[i])
    batches.append(data[i+1])
    batches.append(data[i+2])
    
    print(batches[0])
    
    for char in batches[0]:
        if char not in common_chars:
            if char in batches[1] and char in batches[2]:
                common_chars.append(char)
                s += priorities.index(char)
                
    sums.append(s)

print(sum(sums))
    