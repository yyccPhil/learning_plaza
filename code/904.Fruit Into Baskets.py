#
# @lc app=leetcode id=904 lang=python
# @lcpr version=20003
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (45.14%)
# Likes:    4813
# Dislikes: 365
# Total Accepted:    457.6K
# Total Submissions: 1M
# Testcase Example:  '[1,2,1]'
#
# You are visiting a farm that has a single row of fruit trees arranged from
# left to right. The trees are represented by an integer array fruits where
# fruits[i] is the type of fruit the i^th tree produces.
# 
# You want to collect as much fruit as possible. However, the owner has some
# strict rules that you must follow:
# 
# 
# You only have two baskets, and each basket can only hold a single type of
# fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from
# every tree (including the start tree) while moving to the right. The picked
# fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must
# stop.
# 
# 
# Given the integer array fruits, return the maximum number of fruits you can
# pick.
# 
# 
# Example 1:
# 
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# 
# 
# Example 2:
# 
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# 
# 
# Example 3:
# 
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
    #     left = 0
    #     right = 0
    #     sum = 0
    #     tree_dict = dict()
    #     res = 0

    #     while right < len(fruits):
    #         tree_dict[fruits[right]] = tree_dict.get(fruits[right], 0) + 1
    #         cnt = self.cntTree(tree_dict)
    #         if cnt > 2:
    #             if sum > res:
    #                 res = sum
    #             while self.cntTree(tree_dict) > 2:
    #                 tree_dict[fruits[left]] -= 1
    #                 left += 1
    #                 sum -= 1

    #         sum += 1
    #         right += 1
        
    #     if sum > res:
    #         return sum
    #     else:
    #         return res
        
    # def cntTree(self,tree_dict):
    #     cnt = 0
    #     for i in tree_dict.keys():
    #         if tree_dict[i] > 0:
    #             cnt += 1
    #     return cnt

        l = 0
        r = 0
        tree_dict = dict()
        dict_cnt = 0
        res = 0

        while r < len(fruits):
            if not tree_dict.get(fruits[r]):
                dict_cnt += 1
            tree_dict[fruits[r]] = tree_dict.get(fruits[r], 0) + 1
            
            while dict_cnt > 2:
                if r - l > res:
                    res = r - l
                if tree_dict[fruits[l]] == 1:
                    dict_cnt -= 1
                tree_dict[fruits[l]] -= 1
                l += 1
            
            r += 1
        
        if r - l > res:
            return r - l
        else:
            return res
            


# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,2,2]\n
# @lcpr case=end

#

