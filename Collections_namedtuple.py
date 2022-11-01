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
