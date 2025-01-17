#
# @lc app=leetcode id=116 lang=python3
# @lcpr version=20004
#
# [116] Populating Next Right Pointers in Each Node
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        from collections import deque
        my_que = deque()
        my_que.append(root)
        
        def pop_append(que):
            pop_node = que.popleft()
            if pop_node.left:
                que.append(pop_node.left)
            if pop_node.right:
                que.append(pop_node.right)
        
        while my_que:
            for _ in range(len(my_que)-1):
                my_que[0].next = my_que[1]
                pop_append(my_que)
            my_que[0].next = None
            pop_append(my_que)
        return root
            
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

