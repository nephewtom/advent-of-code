 
directions = ""
with open('input1.txt', 'r', encoding="utf-8") as f:
    directions = f.read()
    
# print(len(directions))

def find_final_floor():
    n = 0
    for c in directions:
        if c == '(':
            n += 1
        elif c == ')':
            n -= 1
    return n
            
floor = find_final_floor()
print(f"floor: {floor}")

def find_first_pos_basement():
    curr = 0
    pos = 1
    for c in directions:
        if c == '(':
            curr += 1
        elif c == ')':
            curr -= 1        

        if curr == -1:
           return pos
       
        pos += 1

pos = find_first_pos_basement()
print(f"pos: {pos}")


