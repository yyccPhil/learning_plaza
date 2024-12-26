#
# @lc app=leetcode id=232 lang=python3
# @lcpr version=20004
#
# [232] Implement Queue using Stacks
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if len(self.stack_out) != 0:
            return self.stack_out.pop()
        while len(self.stack_in) != 0:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        res = self.pop()
        self.stack_out.append(res)
        return res

    def empty(self) -> bool:
        if not (self.stack_out or self.stack_in):
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end



