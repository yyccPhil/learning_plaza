#
# @lc app=leetcode id=24 lang=python3
# @lcpr version=20003
#
# [24] Swap Nodes in Pairs
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy head
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            tmp1 = cur.next
            tmp2 = cur.next.next
            tmp1.next = tmp2.next
            tmp2.next = tmp1
            cur.next = tmp2
            cur = cur.next.next
        return dummy.next

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

