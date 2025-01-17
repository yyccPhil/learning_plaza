#
# @lc app=leetcode id=515 lang=python3
# @lcpr version=20004
#
# [515] Find Largest Value in Each Tree Row
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if not root:
            return res
        from collections import deque
        my_que = deque()
        my_que.append(root)
        
        while my_que:
            level = list()
            for _ in range(len(my_que)):
                out_node = my_que.popleft()
                level.append(out_node.val)
                if out_node.left:
                    my_que.append(out_node.left)
                if out_node.right:
                    my_que.append(out_node.right)
            res.append(max(level))
        return res
            
        
# @lc code=end



#
# @lcpr case=start
# [1,3,2,5,3,null,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

