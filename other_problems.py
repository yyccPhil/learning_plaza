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
  
--------------------------------------------------------------------------------------------

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

--------------------------------------------------------------------------------------------

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
