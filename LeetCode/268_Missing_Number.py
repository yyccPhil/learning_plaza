class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        origin_lst = list(range(len(nums) + 1))
        for i in origin_lst:
            if i not in nums:
                return i
