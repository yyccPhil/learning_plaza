#
# @lc app=leetcode id=541 lang=python3
# @lcpr version=20004
#
# [541] Reverse String II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_lst = list(s)
        for i in range(0,len(s),2*k):
            if len(s) - i < k:
                s_lst[i:] = self.reverse(s_lst[i:])
            else:
                s_lst[i:i+k] = self.reverse(s_lst[i:i+k])
                
        return ''.join(s_lst)

    def reverse(self, lst):
        for i in range(len(lst)//2):
            lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
        return lst
        
# @lc code=end



#
# @lcpr case=start
# "abcdefg"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n2\n
# @lcpr case=end

#

