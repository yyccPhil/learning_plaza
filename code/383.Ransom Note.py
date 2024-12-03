#
# @lc app=leetcode id=383 lang=python3
# @lcpr version=20004
#
# [383] Ransom Note
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_array = [0 for _ in range(26)]
        for c in magazine:
            letter_array[ord(c) - ord('a')] += 1
        for c in ransomNote:
            if letter_array[ord(c) - ord('a')] >= 1:
                letter_array[ord(c) - ord('a')] -= 1
            else:
                return False
        return True
        
        
# @lc code=end



#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

#

