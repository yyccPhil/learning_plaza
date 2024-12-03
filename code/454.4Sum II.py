#
# @lc app=leetcode id=454 lang=python3
# @lcpr version=20004
#
# [454] 4Sum II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums_map = dict()
        for i in nums1:
            for j in nums2:
                nums_map[i+j]=nums_map.get(i+j,0) + 1
        res_cnt = 0
        for i in nums3:
            for j in nums4:
                if -(i+j) in nums_map:
                    res_cnt += nums_map[-(i+j)]
        return res_cnt
        
# @lc code=end



#
# @lcpr case=start
# [1,2]\n[-2,-1]\n[-1,2]\n[0,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n[0]\n[0]\n
# @lcpr case=end

#

