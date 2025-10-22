from collections import namedtuple
import numpy

Instructions = namedtuple('Instructions', ['action', 'begin', 'end'])
Position = namedtuple('Position', ['x', 'y'])

instructions = []
lights = numpy.zeros((1000, 1000), dtype=bool)


with open('input6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip()
        action, begin, dummy, end = map(str, line.split(' '))
        instructions.append(Instructions(action, begin, end))

def parse_position(s: str) -> Position:
    x, y = map(int, s.split(','))
    return Position(x, y)

def execute_instructions():
    print("Looping instructions...")
    for i in range(len(instructions)):
        # print(instructions[i])

        begin = parse_position(instructions[i].begin)
        end = parse_position(instructions[i].end)

        action = instructions[i].action
        for y in range(begin.y, end.y+1):
            for x in range(begin.x, end.x+1):
                if action == 'on':
                    lights[x, y] = True
                elif action == 'off':
                    lights[x, y] = False
                else: # toggle                
                    lights[x, y] = not lights[x, y]


def get_lights_on():
    lights_on = 0
    for y in range(0,1000):
        for x in range(0, 1000):
            if lights[x, y] == True:
                lights_on += 1

    return lights_on

# execute_instructions()
# print("lights_on:", get_lights_on())

lights2 = numpy.zeros((1000, 1000), dtype=int)

def execute_instructions2():
    print("Looping instructions 2...")
    for i in range(len(instructions)):
        # print(instructions[i])

        begin = parse_position(instructions[i].begin)
        end = parse_position(instructions[i].end)

        action = instructions[i].action
        for y in range(begin.y, end.y+1):
            for x in range(begin.x, end.x+1):
                if action == 'on':
                    lights2[x, y] +=1
                elif action == 'off':
                    if lights2[x, y] > 0:
                        lights2[x, y] -= 1
                else: # toggle                
                    lights2[x, y] += 2

                    
def get_total_brightness():
    brightness = 0
    for y in range(0,1000):
        for x in range(0, 1000):
            brightness += lights2[x, y]

    return brightness

execute_instructions2()
print("total brightness:", get_total_brightness())
