#
# @lc app=leetcode id=199 lang=python3
# @lcpr version=20004
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if not root:
            return res
        from collections import deque
        my_que = deque()
        my_que.append(root)
        
        while my_que:
            last_val = 0
            for _ in range(len(my_que)):
                out_node = my_que.popleft()
                last_val = out_node.val
                if out_node.left:
                    my_que.append(out_node.left)
                if out_node.right:
                    my_que.append(out_node.right)
            res.append(last_val)
            
        return res
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

