# Collections.deque()
# A deque is a double-ended queue. It can be used to add or remove elements from both ends.
# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

from collections import deque
d = deque()

for i in range(int(input())):
    com = input().split()
    if len(com) == 1:
        if com[0] == "pop":
            d.pop()
        elif com[0] == "popleft":
            d.popleft()
    else:
        num = int(com[1])
        if com[0] == "append":
            d.append(num)
        elif com[0] == "appendleft":
            d.appendleft(num)

print(*d)
