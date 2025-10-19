from collections import namedtuple
Box = namedtuple('Box', ['l', 'w', 'h'])

boxes = []
with open('input2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip() # remove newline and spaces
        if not line:
            continue # skip empty lines

        l, w, h = map(int, line.split('x'))
        boxes.append(Box(l, w, h))

paper = 0
ribbon = 0
for i in range(0, len(boxes)):
    box = boxes[i]
    
    # print(item)
    base_area = box.l * box.w
    face_one = box.w * box.h
    face_two = box.l * box.h
    extra_paper = min(base_area, face_one, face_two)
    # print("a:", 2*base_area + 2*face_one + 2*face_two + extra_paper)
    paper += 2*base_area + 2*face_one + 2*face_two + extra_paper
    # print(paper, end=', ')

    base_perimeter = 2*box.l + 2*box.w
    face_one_perimeter = 2*box.w + 2*box.h
    face_two_perimeter = 2*box.l + 2*box.h
    ribbon += min(base_perimeter, face_one_perimeter, face_two_perimeter)
    bow = box.l * box.w * box.h
    ribbon += bow
    # print(ribbon, end=', ')
    
print("paper:", paper)
print("ribbon:", ribbon)
