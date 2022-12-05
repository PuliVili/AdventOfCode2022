path = r"/home/vuhl/Projects/AoC2022/Day5/data.txt"
with open(path) as d:
    data = [line.rstrip('\n') for line in d]

'''
[M]                     [N] [Z]    
[F]             [R] [Z] [C] [C]    
[C]     [V]     [L] [N] [G] [V]    
[W]     [L]     [T] [H] [V] [F] [H]
[T]     [T] [W] [F] [B] [P] [J] [L]
[D] [L] [H] [J] [C] [G] [S] [R] [M]
[L] [B] [C] [P] [S] [D] [M] [Q] [P]
[B] [N] [J] [S] [Z] [W] [F] [W] [R]
'''

cols =[['M','F','C','W','T','D','L','B'], ['L','B','N'], ['V','L','T','H','C','J'], ['W','J','P','S'], ['R','L','T','F','C','S','Z'], ['Z','N','H','B','G','D','W'], ['N','C','G','V','P','S','M','F'], ['Z','C','V','F','J','R','Q','W'], ['H','L','M','P','R']]

def move_recursively(from_col, to_col, amount):
    if amount == 0:
        return
    
    else:
        cols[to_col].insert(0, cols[from_col][0])
        cols[from_col].pop(0)
        move_recursively(from_col, to_col, amount-1)
        
def move_in_loop(from_col, to_col, amount):
    for i in range(amount):
        cols[to_col].insert(i, cols[from_col][i])
        
    for i in range(amount):
        cols[from_col].pop(0)


for row in data:
    words = row.split(" ")
    amount = int(words[1])
    from_col = int(words[3]) - 1
    to_col = int(words[5]) -1

    #move_recursively(from_col, to_col, amount)
    move_in_loop(from_col, to_col, amount)


r = ""   
for col in cols:
    r += col[0]
    
print(r)