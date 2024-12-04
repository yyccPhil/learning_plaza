#
# @lc app=leetcode id=350 lang=python
# @lcpr version=20004
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (58.76%)
# Likes:    7784
# Dislikes: 983
# Total Accepted:    1.5M
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times as it
# shows in both arrays and you may return the result in any order.
# 
# 
# Example 1:
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# Example 2:
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
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
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        lst1 = [0 for _ in range(1001)]
        lst2 = [0 for _ in range(1001)]
        res = list()

        for i in nums1:
            lst1[i] += 1
        for i in nums2:
            lst2[i] += 1
        for i in range(1001):
            if lst1[i] * lst2[i] != 0:
                for _ in range(min(lst1[i], lst2[i])):
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

