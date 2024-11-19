#
# @lc app=leetcode id=367 lang=python3
# @lcpr version=20003
#
# [367] Valid Perfect Square
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
        return False
                
        
# @lc code=end



#
# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 14\n
# @lcpr case=end

#

