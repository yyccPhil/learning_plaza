#
# @lc app=leetcode id=20 lang=python3
# @lcpr version=20004
#
# [20] Valid Parentheses
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = list()
        for c in s:
            if c == '(':
                my_stack.append(')')
            elif c == '[':
                my_stack.append(']')
            elif c == '{':
                my_stack.append('}')
            elif len(my_stack) == 0 or c != my_stack[-1]:
                return False
            else:
                my_stack.pop()
        if len(my_stack) == 0:
            return True
        return False
            
        
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#

