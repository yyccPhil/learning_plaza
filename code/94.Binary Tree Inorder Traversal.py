#
# @lc app=leetcode id=94 lang=python3
# @lcpr version=20004
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        my_stack = list()
        def deepLeft(root):
            while root:
                my_stack.append(root)
                if root.left:
                    root = root.left
                else:
                    break
        deepLeft(root)
        while my_stack:
            # res.append(my_stack.pop().val)
            root = my_stack.pop()
            res.append(root.val)
            if root.right:
                deepLeft(root.right)
            
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

