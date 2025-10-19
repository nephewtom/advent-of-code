from dataclasses import dataclass
from dataclasses import astuple
from collections import defaultdict

@dataclass
class Position:
    x: int
    y: int

directions = ""
with open('input3.txt', 'r', encoding='utf-8') as f:
    directions = f.read()

def get_houses_with_present():

    houses = defaultdict(int)
    pos = Position(0, 0)
    houses[astuple(pos)] = 1

    count = 0
    for c in directions:
        # count +=1
        # if count == 10:
        #     break
        if c == '^':
            pos.y += 1
        elif c == 'v':
            pos.y -= 1
        elif c == '>':
            pos.x += 1
        elif c == '<':
            pos.x -= 1

        t = astuple(pos)
        houses[t] += 1
        # print("c:", c, "pos:", t, "n:", houses[t])

    return houses
    
print()
houses_with_present = get_houses_with_present()
print("houses with present:", len(houses_with_present))
# print(houses_with_present)
# houses with present: 2572


def get_houses_robo_santa():

    houses = defaultdict(int)
    pos = Position(0, 0)
    houses[astuple(pos)] = 2
    santa_pos = Position(0, 0)
    robot_pos = Position(0, 0)

    santa_turn = True

    count = 0
    for c in directions:
        # count +=1
        # if count == 10:
        #     break

        pos = santa_pos if santa_turn else robot_pos
        
        if c == '^':
            pos.y += 1
        elif c == 'v':
            pos.y -= 1
        elif c == '>':
            pos.x += 1
        elif c == '<':
            pos.x -= 1

        if santa_turn:
            santa_pos = pos
        else:
            robot_pos = pos

        t = astuple(pos)
        houses[t] += 1

        santa_turn = not santa_turn
        # print("c:", c, "pos:", t, "n:", houses[t])
        
    return houses
        
houses_with_robosanta = get_houses_robo_santa()
print("houses with robosanta:", len(houses_with_robosanta))
