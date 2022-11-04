# focus on optimization

n, m = map(int, input().split())
arr = input().split()
A = set(input().split())
B = set(input().split())

result = 0
# for i in arr:
#     for j in A:
#         if i == j:
#             result += 1
#     for k in B:
#         if i == k:
#             result -= 1
for i in arr:
    if i in A:
        result += 1
    if i in B:
        result -= 1
        
# A = [1 if i in A else 0 for i in arr]
# B = [1 if i in B else 0 for i in arr]
# result = sum(A) - sum(B)
# I am not sure which one is faster? Maybe first?
        
print(result)
