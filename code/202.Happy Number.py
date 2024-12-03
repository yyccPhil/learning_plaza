#
# @lc app=leetcode id=202 lang=python3
# @lcpr version=20004
#
# [202] Happy Number
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        next_n = n
        n_set = set()
        n_set.add(n)
        while next_n != 1:
            n_str = str(next_n)
            n_lst = list()
            for n_chr in n_str:
                n_lst.append(int(n_chr))
            next_n = 0
            for i in n_lst:
                next_n += i * i
            if next_n in n_set:
                return False
            n_set.add(next_n)
        return True
        
# @lc code=end



#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

