#
# @lc app=leetcode id=349 lang=python
# @lcpr version=20004
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (75.58%)
# Likes:    6234
# Dislikes: 2305
# Total Accepted:    1.4M
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
# 
# 
# Example 1:
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# Example 2:
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # return list(set(nums1) & set(nums2))

        lst1 = [0 for _ in range(1001)]
        for i in nums1:
            lst1[i] += 1
        res = list()
        for i in nums2:
            if lst1[i] != 0:
                lst1[i] = 0
                res.append(i)
        return res
        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#

