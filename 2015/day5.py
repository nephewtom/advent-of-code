strings = []

with open('input5.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        strings.append(line)

print(len(strings))


def has_three_vowels(s):
    vowels = 'aeiou'
    # ch in vowels returns True/False that is converted to 1/0
    return sum(ch in vowels for ch in s) >= 3

def has_double_letter(s):
    # any returns True 
    return any(s[i] == s[i+1] for i in range(len(s) - 1))

def has_not_forbidden_strings(s):
    forbidden = [ 'ab', 'cd', 'pq', 'xy' ]
    return not any(f in s for f in forbidden)

# print(has_three_vowels('aae'))
# print(has_three_vowels('abc'))
# print(has_double_letter('abc'))
# print(has_double_letter('aab'))
# print(has_not_forbidden_strings('abdc'))
# print(has_not_forbidden_strings('xydc'))
# print(has_not_forbidden_strings('aydc'))

def get_nice_part1():
    total = 0
    for s in strings:
        if has_three_vowels(s) and has_double_letter(s) and has_not_forbidden_strings(s):
            total += 1
    return total


def has_repeated_pair(s):
    for i in range(len(s)-2):
        t = s[i]+s[i+1]
        # print(t, "in", s[i+2:len(s)]);
        if t in s[i+2:len(s)]:
            return True
    return False

def has_repeated_letter_in_between(s):
    return any(s[i] == s[i+2] for i in range(len(s)-2))

def is_nice2(s):
    return has_repeated_pair(s) and has_repeated_letter_in_between(s)

# print(has_repeated_pair('abxxab'))
# print(has_repeated_pair('abbcd'))
# print(has_repeated_pair('aaa'))
# print(has_repeated_letter_in_between('ababab'))
# print(has_repeated_letter_in_between('abcdef'))

e1 = 'qjhvhtzxzqqjkmpb'
e2 = 'xxyxx'
e3 = 'uurcxstgmygtbstg'
e4 = 'ieodomkazucvgmuy'

print('e1')
print(has_repeated_letter_in_between(e1))
print(has_repeated_pair(e1))

print('e1', is_nice2(e1))
print('e2', is_nice2(e2))
print('e3', is_nice2(e3))
print('e4', is_nice2(e4))

def get_nice_part2():
    total = 0
    for s in strings:
        if is_nice2(s):
            total += 1
    return total

# total_nice = get_nice_part1()
total_nice = get_nice_part2()
print("total nice:", total_nice)


