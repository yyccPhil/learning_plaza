#
# @lc app=leetcode id=225 lang=python3
# @lcpr version=20004
#
# [225] Implement Stack using Queues
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque

class MyStack:
    
    def __init__(self):
        self.que_in = deque()
        self.que_out = deque()

    def push(self, x: int) -> None:
        self.que_in.append(x)

    def pop(self) -> int:
        while len(self.que_in) > 1:
            self.que_out.append(self.que_in.popleft())
        res = self.que_in.pop()
        self.que_in, self.que_out = self.que_out, self.que_in
        return res

    def top(self) -> int:
        res = self.pop()
        self.push(res)
        return res

    def empty(self) -> bool:
        if len(self.que_in) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end



