path = r"/home/vuhl/Projects/AoC2022/Day4/data.txt"
with open(path) as d:
    data = [line.rstrip('\n') for line in d]

r_1 = 0
r_2 = 0

for row in data:
    seq_1, seq_2 = row.split(",")
    min_seq_1, max_seq_1 = seq_1.split("-")
    min_seq_2, max_seq_2 = seq_2.split("-")
    
    max_seq_1 = int(max_seq_1)
    min_seq_1 = int(min_seq_1)
    max_seq_2 = int(max_seq_2)
    min_seq_2 = int(min_seq_2)
    
    if min_seq_1 >= min_seq_2 and max_seq_1 <= max_seq_2:
        r_1 += 1

    elif min_seq_2 >= min_seq_1 and max_seq_2 <= max_seq_1:
        r_1 += 1
        
    if not(min_seq_1 > max_seq_2 or min_seq_2 > max_seq_1):
        r_2 += 1
    
print(r_1)
print(r_2)