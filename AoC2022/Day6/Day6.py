path = r"/home/vuhl/Projects/AoC2022/Day6/data.txt"
with open(path) as d:
    data = [line.rstrip('\n') for line in d]

while True:
    batch = []
    for row in data:
        for count, char in enumerate(row):
            batch.append(char)
            
            if len(batch) > 14:
                batch.pop(0)

            temp_set = set(batch)
            
            if len(temp_set) == 14:
                print(count + 1)
                break
                
        break
    break


