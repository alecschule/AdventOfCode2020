from collections import deque
from itertools import islice

with open('input.txt') as f:
    parts = f.read().split('\n\n')

p1 = deque(int(i) for i in parts[0].splitlines()[1:])
p2 = deque(int(i) for i in parts[1].splitlines()[1:])

def part_one(p1, p2):
    while min(len(p1), len(p2)) > 0:
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 > c2: p1.extend((c1, c2))
        else: p2.extend((c2, c1))
    winner = p2 if len(p1) == 0 else p1
    print(sum(card * (len(winner) - index) for index, card in enumerate(winner)))

# returns true for p1 win
def game(p1, p2):
    prev_rounds = set()
    while min(len(p1), len(p2)) > 0:
        round_hash = hash(tuple(p1)) + hash(tuple(p2))
        if round_hash in prev_rounds: return (True, p1)
        prev_rounds.add(round_hash)
        c1 = p1.popleft()
        c2 = p2.popleft()
        if len(p1) >= c1 and len(p2) >= c2:
            p1win = game(deque(islice(p1, 0, c1)), deque(islice(p2, 0, c2)))[0]
        else:
            p1win = c1 > c2
        if p1win: p1.extend((c1, c2))
        else: p2.extend((c2, c1))
    # one deck is empty
    p1win = len(p1) > 0
    return (p1win, p1 if p1win else p2) 

def part_two(p1, p2):
    winner = game(p1, p2)[1]
    print(sum(card * (len(winner) - index) for index, card in enumerate(winner)))
    
# part_one(deque(p1), deque(p2))
part_two(p1, p2)
