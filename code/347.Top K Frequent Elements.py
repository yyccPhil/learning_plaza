#
# @lc app=leetcode id=347 lang=python3
# @lcpr version=20004
#
# [347] Top K Frequent Elements
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash = dict()
        for i in nums:
            my_hash[i] = my_hash.get(i,0) + 1
        # fre_lst = sorted(list(my_hash.values()),reverse=True)[:k]
        
        # res = list()
        # for key in my_hash:
        #     if my_hash[key] in fre_lst:
        #         res.append(key)
                
        # return res
        pri_que = list()
        for key, freq in my_hash.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        res = list()
        for i in range(k-1,-1,-1):
            res.append(heapq.heappop(pri_que)[1])
        return res
        
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

