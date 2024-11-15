#
# @lc app=leetcode id=977 lang=python3
# @lcpr version=20003
#
# [977] Squares of a Sorted Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        p1, p2 = 0, nums_len - 1
        p = nums_len - 1
                
        res_lst = [0] * nums_len
        
        while p1 <= p2:
            if abs(nums[p1]) > abs(nums[p2]):
                res_lst[p] = nums[p1] * nums[p1]
                p1 += 1
            else:
                res_lst[p] = nums[p2] * nums[p2]
                p2 -= 1
            p -= 1
        
        return res_lst
            
        
        
# @lc code=end



#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#

