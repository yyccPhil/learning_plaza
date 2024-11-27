#
# @lc app=leetcode id=206 lang=python3
# @lcpr version=20003
#
# [206] Reverse Linked List
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
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     cur = head
    #     pre = None
    #     while cur:
    #         temp = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = temp
    #     return pre

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
    
    def reverse(self, cur, pre):
        if not cur:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

