import os
from collections import namedtuple

Wire = namedtuple('Wire', ['signal', 'value'])
wires = {}

Operation = namedtuple('Operation', ['i1', 'gate', 'i2', 'dest'])
operations = []

print('Starting...')
print(wires)


def parse_operation(op : str, dest : str) -> Operation :

    o = None
    wires[dest] = Wire(False, 0)
    
    spaces = op.count(' ')
    if spaces == 0: # single set operation
        if op.isdigit():
            wires[dest] = Wire(True, int(op))
        else:
            o = Operation('0', 'SET', op, dest)
            
    elif spaces == 1: # NOT operation
        w = op.split(' ')[1]
        o = Operation('0', 'NOT', w, dest)

    elif spaces== 2:
        i1, gate, i2 = map(str, op.split(' '))
        o = Operation(i1, gate, i2, dest)        

    return o

def parse_input():
    with open('input7.txt', 'r', encoding='utf-8') as f:
        print('Parsing...')
        for line in f:
            line = line.rstrip()
            op, dest = map(str, line.split(' -> '))

            obj = parse_operation(op, dest)
            if obj :
                operations.append(obj)

    print("n wires:", len(wires.keys()))
    print("n operations:", len(operations))

def print_operations():
    for i in range(len(operations)):    
        print(operations[i])

def print_wires():
    for key, value in wires.items():
        print(key, ':', value)

def print_wires_with_signal():
    print('--- Wires with signal')
    for key, value in wires.items():
        if value.signal:
            print('|', key, ':', value.value)

def run_operations():
    print('--- loop operations')
    for i in range(len(operations)):
        op = operations[i]
        # print(op)
        gate = op.gate
        i1 = wires.get(op.i1)
        if i1 == None:
            i1 = Wire(True, int(op.i1))
        i2 = wires.get(op.i2)
        if i2 == None:
            i2 = Wire(True, int(op.i2))
        dest = op.dest
        # print(op.i1, '[', i1, ']', gate, '[', i2, '] ->', dest)

        if gate == 'NOT' and i2.signal:
            wires[dest] = Wire(True, ~i2.value)
            operations.pop(i)
            break

        if gate == 'SET' and i2.signal:
            wires[dest] = Wire(True, i2.value)
            operations.pop(i)
            break
        
        elif gate == 'RSHIFT' and i1.signal:
            wires[dest] = Wire(True, i1.value >> i2.value)
            operations.pop(i)
            break

        elif gate == 'LSHIFT' and i1.signal:
            wires[dest] = Wire(True, i1.value << i2.value)
            operations.pop(i)
            break

        elif gate == 'OR' and i1.signal and i2.signal:
            wires[dest] = Wire(True, i1.value | i2.value)
            operations.pop(i)
            break    

        elif gate == 'AND' and i1.signal and i2.signal:
            wires[dest] = Wire(True, i1.value & i2.value)
            operations.pop(i)
            break    
        
    print(op.i1, '[', i1, ']', gate, '[', i2, '] ->', dest)
    if len(operations) > 0:
        # print_wires()
        # print_operations()
        # print_wires_with_signal()
        print('operations remaing:', len(operations))
        
        # kk = input('$>')
        run_operations()


# part 1
parse_input()
print_wires_with_signal()
run_operations()

a = wires['a'].value
print('a:', wires['a'])

# part 2
parse_input()
wires['b'] = Wire(True, a)

print_wires_with_signal()
run_operations()

a = wires['a'].value
print('a:', wires['a'])
