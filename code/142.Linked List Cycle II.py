#
# @lc app=leetcode id=142 lang=python3
# @lcpr version=20004
#
# [142] Linked List Cycle II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return None
        slow, fast = head.next, head.next.next
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

