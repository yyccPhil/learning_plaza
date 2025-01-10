#
# @lc app=leetcode id=145 lang=python3
# @lcpr version=20004
#
# [145] Binary Tree Postorder Traversal
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if not root:
            return res
        my_stack = [root]
        while my_stack:
            mid = my_stack.pop()
            res.append(mid.val)
            if mid.left:
                my_stack.append(mid.left)
            if mid.right:
                my_stack.append(mid.right)
        res.reverse()
        return res
        
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,null,8,null,null,6,7,9]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

