import hashlib

input = 'yzbqklnj'
# input = 'abcdef'

def find_number_for_hash(zeroes : int, max_decimal : int):
    for i in range(0, max_decimal):
    
        msg = input + str(i)
        res = hashlib.md5(msg.encode())

        hash = res.hexdigest()

        found = True
        for j in range(0, zeroes):
            if hash[j] != '0':
                found = False
                break

        if found:
            return i

    return 0

print(find_number_for_hash(5, 1000000))
print(find_number_for_hash(6, 10000000))
