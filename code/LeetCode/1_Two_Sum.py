class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = set()

        for i in range(len(nums)):
            if target - nums[i] in seen:
                j = nums.index(target - nums[i])
                return [min(i,j), max(i,j)]
            
            else:
                seen.add(nums[i])
