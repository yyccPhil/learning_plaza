#
# @lc app=leetcode id=160 lang=python3
# @lcpr version=20003
#
# [160] Intersection of Two Linked Lists
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1 = headA
        cur2 = headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1

        
# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

