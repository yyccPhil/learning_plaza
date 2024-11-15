#
# @lc app=leetcode id=844 lang=python3
# @lcpr version=20003
#
# [844] Backspace String Compare
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if self.backspace(s) == self.backspace(t):
            return True
        else:
            return False
    
    def backspace(self, s: str) -> str:
        s_list = list()
        slow = 0
        for fast in range(len(s)):
            if s[fast] != '#':
                s_list.append(s[fast])
                slow += 1
            else:
                if slow - 1 >= 0:
                    s_list.pop()
                    slow -= 1
        return ''.join(s_list)
        
# @lc code=end



#
# @lcpr case=start
# "ab#c"\n"ad#c"\n
# @lcpr case=end

# @lcpr case=start
# "ab##"\n"c#d#"\n
# @lcpr case=end

# @lcpr case=start
# "a#c"\n"b"\n
# @lcpr case=end

#

