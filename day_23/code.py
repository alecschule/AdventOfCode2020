inpt = 974618352
num_cups = 1000000

class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None

class Cups:
    def __init__(self, seed, num):
        seed_cups = [int(i) for i in str(seed)]
        first_node = Node(seed_cups[0])
        self.head = first_node
        self.current_node = first_node
        self.current_index = 0
        self.tail = first_node
        for i in seed_cups[1:]: self.append(i)
        for i in range(max(seed_cups)+1, num+1): self.append(i)
    def append(self, data):
        new_node = Node(data)
        self.tail.nxt = new_node
        self.tail = new_node
    def access(self, index):
        if index < self.current_index:
            self.current_node = self.head
            self.current_index = 0
        for i in range(index-self.current_index):
            self.current_node = self.current_node.nxt
            self.current_index += 1
        return self.current_node.data
    def find(self, data):
        while self.current_node.data != data:
            self.current_node = self.current_node.nxt
            self.current_index += 1
            if self.current_node is None:
                self.current_node = self.head
                self.current_index = 0
        return self.current_index
    def remove(self, index):
        if index == 0:
            val = self.head.data
            self.head = self.head.nxt
            return val
        if index <= self.current_index:
            self.current_node = self.head
            self.current_index = 0
        for i in range(index-self.current_index-1):
            self.current_node = self.current_node.nxt
            self.current_index += 1
        val = self.current_node.nxt.data
        next_node = self.current_node.nxt.nxt
        self.current_node.nxt = next_node
        return val
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.nxt = self.head
            self.head = new_node
            if self.current_index != 0: self.current_index += 1
        if index <= self.current_index:
            self.current_node = self.head
            self.current_index = 0
        for i in range(index-self.current_index-1):
            self.current_node = self.current_node.nxt
            self.current_index += 1
        new_node.nxt = self.current_node.nxt
        self.current_node.nxt = new_node

my_cups = Cups(inpt, num_cups)
active_index = 0
def move_cups():
    global my_cups
    global active_index
    current_num = my_cups.access(active_index)
    removed = []
    for i in range(3):
        if active_index+1 >= num_cups-i: active_index = -1
        removed.append(my_cups.remove(active_index+1))
    next_num = current_num - 1 if current_num != 1 else num_cups
    while next_num in removed:
        next_num -= 1
        if next_num <= 0:
            next_num = num_cups
    destination = my_cups.find(next_num) + 1
    for i in reversed(removed):
        my_cups.insert(destination, i)
    active_index = my_cups.find(current_num) + 1
    if active_index == num_cups: active_index = 0

for i in range(10000000):
    if i % 1000 == 0: print(i)
    move_cups()

#index_one = my_cups.find(1)
#for i in range(1, num_cups): print(my_cups.access((index_one + i) % num_cups), end='')

print(cups.access((cups.find(1) + 1) % len(cups)) * cups.access((cups.find(1) + 2) % len(cups)))
