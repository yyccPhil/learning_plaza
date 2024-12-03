#
# @lc app=leetcode id=242 lang=python3
# @lcpr version=20004
#
# [242] Valid Anagram
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_lst = list()
        # for chr in s:
        #     s_lst.append(chr)
        # for chr in t:
        #     if chr in s_lst:
        #         s_lst.remove(chr)
        #     else:
        #         return False
        # if len(s_lst) != 0:
        #     return False
        # else:
        #     return True
        letter_lst = [0 for _ in range(26)]
        for chr in s:
            letter_lst[ord(chr) - ord('a')] += 1
        for chr in t:
            if letter_lst[ord(chr) - ord('a')] > 0:
                letter_lst[ord(chr) - ord('a')] -= 1
            else:
                return False
        for l in letter_lst:
            if l != 0:
                return False
        return True
        
# @lc code=end



#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#

