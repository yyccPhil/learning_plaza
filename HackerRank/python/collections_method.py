# Collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

from collections import Counter

X = int(input())
size_lst = Counter(list(map(int, input().split())))
N = int(input())
target_lst = list()

prize = 0
for i in range(N):
    size, pay = map(int, input().split())
    if size_lst.get(size):
        prize += pay
        size_lst[size] -= 1

print(prize)

# --------------------------------------------------------------------------------------------

# Collections.namedtuple()

# from collections import namedtuple
# n = int(input())
# stu = namedtuple("stu", input())
# marks = 0
# for i in range(n):
#     marks += int(stu(*input().split()).MARKS)
# print("%.2f" % (marks/n))

# Can you solve this challenge in 4 lines of code or less?
from collections import namedtuple
n, stu = int(input()), namedtuple("stu", input())   # ***
mark_lst = [int(stu(*input().split()).MARKS) for i in range(n)]
print("%.2f" % (sum(mark_lst)/n))                   # ***sum(list)

# --------------------------------------------------------------------------------------------

# Collections.OrderedDict()

from collections import OrderedDict

shop_dict = OrderedDict()
for i in range(int(input())):
    item_price = input().split()
    item = " ".join(item_price[:-1])
    price = int(item_price[-1])
    shop_dict[item] = shop_dict.get(item, 0) + price
    
for i in shop_dict:
    print(i, end = ' ')
    print(shop_dict[i])

# --------------------------------------------------------------------------------------------

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
