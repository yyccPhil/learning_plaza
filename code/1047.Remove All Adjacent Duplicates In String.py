#
# @lc app=leetcode id=1047 lang=python3
# @lcpr version=20004
#
# [1047] Remove All Adjacent Duplicates In String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        # my_stack = list()
        # for c in s:
        #     if not my_stack or c != my_stack[-1]:
        #         my_stack.append(c)
        #     else:
        #         my_stack.pop()
        # return ''.join(my_stack)

        s_lst = list(s)
        top = -1
        for i in range(len(s)):
            if top < 0 or s_lst[top] != s_lst[i]:
                top += 1
                s_lst[top] = s_lst[i]
            else:
                top -= 1
        return ''.join(s_lst[:top+1])

        
# @lc code=end



#
# @lcpr case=start
# "abbaca"\n
# @lcpr case=end

# @lcpr case=start
# "azxxzy"\n
# @lcpr case=end

#

