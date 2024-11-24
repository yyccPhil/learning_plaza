#
# @lc app=leetcode id=54 lang=python
# @lcpr version=20003
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (51.94%)
# Likes:    15331
# Dislikes: 1377
# Total Accepted:    1.7M
# Total Submissions: 3.2M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        nums = list()

        while True:
            if top > bottom:
                break
            for j in range(left,right+1):
                nums.append(matrix[top][j])
            top += 1

            if left > right:
                break
            for i in range(top,bottom+1):
                nums.append(matrix[i][right])
            right -=1

            if top > bottom:
                break
            for j in range(right,left - 1, -1):
                nums.append(matrix[bottom][j])
            bottom -= 1

            if left > right:
                break
            for i in range(bottom,top - 1, -1):
                nums.append(matrix[i][left])
            left +=1

        return nums

        
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

