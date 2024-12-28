#
# @lc app=leetcode id=1207 lang=python
# @lcpr version=20004
#
# [1207] Unique Number of Occurrences
#
# https://leetcode.com/problems/unique-number-of-occurrences/description/
#
# algorithms
# Easy (77.81%)
# Likes:    5200
# Dislikes: 143
# Total Accepted:    754.2K
# Total Submissions: 969.2K
# Testcase Example:  '[1,2,2,1,1,3]'
#
# Given an array of integers arr, return true if the number of occurrences of
# each value in the array is unique or false otherwise.
# 
# 
# Example 1:
# 
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
# values have the same number of occurrences.
# 
# Example 2:
# 
# Input: arr = [1,2]
# Output: false
# 
# 
# Example 3:
# 
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        my_hash = dict()
        for i in arr:
            my_hash[i] = my_hash.get(i,0) + 1
        my_set = set()
        for i in my_hash.values():
            if i not in my_set:
                my_set.add(i)
            else:
                return False
        return True
        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# [-3,0,1,-3,1,1,1,-3,10,0]\n
# @lcpr case=end

#

