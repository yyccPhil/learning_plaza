#
# @lc app=leetcode id=59 lang=python
# @lcpr version=20003
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (72.44%)
# Likes:    6515
# Dislikes: 268
# Total Accepted:    634.1K
# Total Submissions: 875.4K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# 
# Example 1:
# 
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        nums = [[0] * n for _ in range(n)]
        cnt = 1

        for round in range(n//2):
            for j in range(round, n-1-round):
                nums[round][j] = cnt
                cnt += 1
            for i in range(round, n-1-round):
                nums[i][j+1] = cnt
                cnt += 1
            for j in range(n-1-round,round, -1):
                nums[i+1][j] = cnt
                cnt += 1
            for i in range(n-1-round,round, -1):
                nums[i][j-1] = cnt
                cnt += 1

        if n%2 != 0:
            nums[n//2][n//2] = cnt

        return nums
        



# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

