#
# @lc app=leetcode id=209 lang=python3
# @lcpr version=20003
#
# [209] Minimum Size Subarray Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    
        # sub_len = len(nums) + 1
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum >= s:
        #             temp = j - i + 1
        #             if temp < sub_len:
        #                 sub_len = temp
        #                 sub = nums[i:j+1]
        #             break

        sub_len= len(nums) + 1
        left = 0
        right = 0
        sum = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                tmp_len = right - left + 1
                if tmp_len < sub_len:
                    sub_len = tmp_len
                sum -= nums[left]
                left += 1
            right += 1
        if sub_len > len(nums):
            return 0
        else:
            return sub_len
                
        
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

