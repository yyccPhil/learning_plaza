#
# @lc app=leetcode id=27 lang=python3
# @lcpr version=20003
#
# [27] Remove Element
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
                    
        return slow
                
        
# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

