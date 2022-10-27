# Enter your code here. Read input from STDIN. Print output to STDOUT

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
