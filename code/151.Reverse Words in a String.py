#
# @lc app=leetcode id=151 lang=python3
# @lcpr version=20004
#
# [151] Reverse Words in a String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
    #     s = s.strip()
    #     s = self.reverse(s).split()
    #     res_lst = list()
    #     for w in s:
    #         res_lst.append(self.reverse(w))
    #     return ' '.join(res_lst)
    
    # def reverse(self, s: str) -> str:
    #     s = list(s)
    #     for i in range(len(s)//2):
    #         s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
    #     return ''.join(s)
        s = s.split()
        for i in range(len(s)//2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        return ' '.join(s)
        
# @lc code=end



#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#

