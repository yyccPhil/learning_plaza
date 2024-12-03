#
# @lc app=leetcode id=438 lang=python3
# @lcpr version=20004
#
# [438] Find All Anagrams in a String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # p_len = len(p)
        # p_lst = [0 for _ in range(26)]
        # for chr in p:
        #     p_lst[ord(chr)-ord('a')] += 1
        
        # res = list()
        # for i in range(len(s) - p_len + 1):
        #     tmp = s[i:i+p_len]
        #     tmp_lst = p_lst.copy()
        #     for chr in tmp:
        #         tmp_lst[ord(chr)-ord('a')] -= 1
        #     flag = 1
        #     for j in tmp_lst:
        #         if j != 0:
        #             flag = 0
        #             break
        #     if flag:
        #         res.append(i)

        # return res
        p_len = len(p)
        p_cnt = Counter(p)
        
        window_str = s[:p_len]
        window_cnt = Counter(window_str)
        
        res = list()
        
        for i in range(len(s) - p_len + 1):
            if window_cnt == p_cnt:
                res.append(i)
            if i+p_len == len(s):
                break
            window_cnt[s[i]] -= 1
            if window_cnt[s[i+p_len]]:
                window_cnt[s[i+p_len]] += 1
            else:
                window_cnt[s[i+p_len]] = 1

        return res
        
# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

