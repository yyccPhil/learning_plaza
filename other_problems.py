# The Minion Game

def minion_game(string):
    # your code goes here
    cap_alpha = [chr(dec) for dec in range(65, 91)]
    v_lst = ["A", "E", "I", "O", "U"]
    
    s_cnt = 0
    k_cnt = 0
    
    for i in range(len(string)):
        if string[i] in v_lst:
            k_cnt += len(string) - i
        else:
            s_cnt += len(string) - i
    
    if k_cnt > s_cnt:
        print("Kevin {}".format(k_cnt))
    elif k_cnt < s_cnt:
        print("Stuart {}".format(s_cnt))
    else:
        print("Draw")
  
# --------------------------------------------------------------------------------------------

# itertools.product()

from itertools import product

a = map(int, input().split())
b = map(int, input().split())

# result_lst = list(product(a, b))

# print(result_lst[0], end = "")
# for i in range(1, len(result_lst)):
#     print(" ", end = "")
#     print(result_lst[i], end = "")

print(*product(a, b))

# --------------------------------------------------------------------------------------------

# itertools.permutations()

from itertools import permutations

s, r = input().split()
s = list(s)
r = int(r)

result_lst = list(permutations(s, r))

# for i in range(len(result_lst)):
#     result_lst[i] = "".join(result_lst[i])

result_lst = ["".join(result_lst[i]) for i in range(len(result_lst))]
    
for result in sorted(result_lst):
    print(result)

# --------------------------------------------------------------------------------------------
    
# Polar Coordinates

import cmath

z = complex(input())

r = abs(z)
fi = cmath.phase(z)

print("{:.3f}".format(r))
print("{:.3f}".format(fi))

# --------------------------------------------------------------------------------------------

# Introduction to Sets

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

    
# --------------------------------------------------------------------------------------------

# DefaultDict Tutorial

from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    d[input()].append(str(i + 1))

for i in range(m):
    check = input()
    if d.get(check):
        print(" ".join(d[check]))
    else:
        print(-1)
        
# --------------------------------------------------------------------------------------------

# Calendar Module

import calendar

month, day, year = map(int, input().split())
print(calendar.weekheader(15).split()[calendar.weekday(year, month, day)].upper())

# --------------------------------------------------------------------------------------------

# Find Angle MBC

import math

AB = int(input())
BC = int(input())
print("{}\N{DEGREE SIGN}".format(round(180/math.pi * math.atan(AB/BC))))


# --------------------------------------------------------------------------------------------

# Symmetric Difference

M = input()
m = set(map(int, input().split()))
N = input()
n = set(map(int, input().split()))

u = m.difference(n).union(n.difference(m))
# u = m.union(n)
# for i in m.intersection(n):
#     u.discard(i)

# for i in sorted(list(u)):
for i in sorted(u):
    print(i)

# --------------------------------------------------------------------------------------------

# itertools.combinations()

from itertools import combinations
S, k = input().split()
S = sorted(list(S))
k = int(k)
for i in range(1, k+1):
    for j in combinations(S, i):
        print("".join(j))
        
# --------------------------------------------------------------------------------------------
      
# Set .add()

stamp = set()
for i in range(int(input())):
    stamp.add(input())
print(len(stamp))

# --------------------------------------------------------------------------------------------
      
# itertools.combinations_with_replacement()

from itertools import combinations_with_replacement
S, k = input().split()
S = sorted(S)
k = int(k)
for i in combinations_with_replacement(S,k):
    print("".join(i))

# --------------------------------------------------------------------------------------------
      
# Word Order
    
from collections import OrderedDict

s = OrderedDict()
for i in range(int(input())):
    w = input()
    s[w] = s.get(w, 0) + 1
    
print(len(s))
print(*s.values())

# s = dict()
# w_lst = list()
# for i in range(int(input())):
#     w = input()
#     if not s.get(w):
#         w_lst.append(w)
#     s[w] = s.get(w, 0) + 1
    
# print(len(s))
# for i in w_lst:
#     print(s[i], end = " ")

# --------------------------------------------------------------------------------------------

# Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    com = input().split()
    if len(com) == 1:
        s.pop()
    else:
        if com[0] == "remove":
            s.remove(int(com[1]))
        else:
            s.discard(int(com[1]))
print(sum(s))

# --------------------------------------------------------------------------------------------

# Compress the String!

from itertools import groupby
print(*[(len(list(g)), int(k)) for k, g in groupby(input())])

# res = list()
# for k, g in groupby(input()):
#     res.append((len(list(g)), int(k)))
# print(*res)

# --------------------------------------------------------------------------------------------

# Set .union() Operation

n = input()
N = set(input().split())
b = input()
B = set(input().split())
# print(len(N.union(B)))
print(len(N|B))

# --------------------------------------------------------------------------------------------

# Triangle Quest 2

