#
# @lc app=leetcode id=239 lang=python3
# @lcpr version=20004
#
# [239] Sliding Window Maximum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque

class MyQueue:
    def __init__(self):
        self.my_queue = deque()
    def my_pop(self,x):
        if self.my_queue[0] == x:
            self.my_queue.popleft()
    def my_push(self,x):
        # 注意必须是小于！不可pop掉相同大小的值，因为若因加入相同值而pop掉了之前的值，
        # 在需要pop前一个相同值时，就会把里面的值pop掉了
        while self.my_queue and self.my_queue[-1] < x:
            self.my_queue.pop()
        self.my_queue.append(x)
    def get_max(self):
        return self.my_queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        my_queue = MyQueue()
        for i in range(k):
            my_queue.my_push(nums[i])
        res = list()
        res.append(my_queue.get_max())
        
        for i in range(len(nums)-k):
            my_queue.my_pop(nums[i])
            my_queue.my_push(nums[i+k])
            res.append(my_queue.get_max())
            
        return res
        
# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

