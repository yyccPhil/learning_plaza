#
# @lc app=leetcode id=707 lang=python3
# @lcpr version=20003
#
# [707] Design Linked List
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# Singly LinkedList
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(None)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy
        for _ in range(index + 1):
            cur = cur.next
        return cur.val
        
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        cur = self.dummy
        for _ in range(self.size):
            cur = cur.next
        # new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif 0 <= index < self.size:
            new_node = ListNode(val)
            cur = self.dummy
            for _ in range(index):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
        cur.next.val = None
        cur.next = cur.next.next
        self.size -= 1


# Doubly LinkedList
class ListNode:
    def __init__(self, val=None, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode(None)
        self.dummy_tail = ListNode(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index <= self.size // 2:
            cur = self.dummy_head
            for _ in range(index + 1):
                cur = cur.next
        else:
            cur = self.dummy_tail
            for _ in range(self.size - index):
                cur = cur.pre
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy_head.next
        new_node.pre = self.dummy_head
        self.dummy_head.next.pre = new_node
        self.dummy_head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy_tail
        new_node.pre = self.dummy_tail.pre
        self.dummy_tail.pre.next = new_node
        self.dummy_tail.pre = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index <= self.size // 2:
            cur = self.dummy_head
            for _ in range(index + 1):
                cur = cur.next
        else:
            cur = self.dummy_tail
            for _ in range(self.size - index):
                cur = cur.pre
        new_node = ListNode(val)
        new_node.next = cur
        new_node.pre = cur.pre
        cur.pre.next = new_node
        cur.pre = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index <= self.size // 2:
            cur = self.dummy_head
            for _ in range(index + 1):
                cur = cur.next
        else:
            cur = self.dummy_tail
            for _ in range(self.size - index):
                cur = cur.pre
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
        cur.val = None
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end



