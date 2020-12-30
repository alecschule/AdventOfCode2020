SUBJECT_NUMBER = 7
MOD_VAL = 20201227

with open('input.txt') as f:
    card_pub, door_pub = tuple(int(i) for i in f.read().splitlines())

def find_loop_size(pub_key):
    global SUBJECT_NUMBER, MOD_VAL
    loop_size = 0
    remainder = 1
    while remainder != pub_key:
        loop_size += 1
        remainder = remainder * SUBJECT_NUMBER % MOD_VAL
    return loop_size

def get_key(loop_size, number):
    global  MOD_VAL
    result = 1
    for i in range(loop_size):
        result = result*number % MOD_VAL
    return result

print(get_key(find_loop_size(card_pub), door_pub))
