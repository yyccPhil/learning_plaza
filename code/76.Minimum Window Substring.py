#
# @lc app=leetcode id=76 lang=python3
# @lcpr version=20003
#
# [76] Minimum Window Substring
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = dict()
        window = dict()
        for chr in t:
            need[chr] = need.get(chr, 0) + 1
        
        valid_need_cnt = len(need)
        valid_cnt = 0
        
        left = 0
        right = 0
        sub_len = len(s) + 1
        sub_res = ""
        
        while right < len(s):
            c = s[right]
            if c in need.keys():
                window[c] = window.get(c,0) + 1
                if window[c] == need[c]:
                    valid_cnt += 1
            
            while valid_cnt == valid_need_cnt:
                temp_res = s[left:right + 1]
                if len(temp_res) < sub_len:
                    sub_len = len(temp_res)
                    sub_res = temp_res
                if s[left] in window.keys():
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        valid_cnt -= 1
                left += 1
            right += 1
        
        if sub_len > len(s):
            return ''
        else:
            return sub_res
        
    # def minWindow(self, s: str, t: str) -> str:
    #     need = dict()
    #     window = dict()
    #     for chr in t:
    #         need[chr] = need.get(chr, 0) + 1
    #         window[chr] = 0
        
    #     valid_need_cnt = len(need)
        
    #     left = 0
    #     right = 0
    #     sub_len = len(s) + 1
    #     sub_res = ""
        
    #     while right < len(s):
    #         if s[right] in window.keys():
    #             window[s[right]] += 1
            
    #         while self.isValid(window,need) == valid_need_cnt:
    #             temp_res = s[left:right + 1]
    #             if len(temp_res) < sub_len:
    #                 sub_len = len(temp_res)
    #                 sub_res = temp_res
    #             if s[left] in window.keys():
    #                 window[s[left]] -= 1
    #             left += 1
    #         right += 1
        
    #     if sub_len > len(s):
    #         return ''
    #     else:
    #         return sub_res
    
    # def isValid(self, window, need):
    #     valid_cnt = 0
    #     for chr in need.keys():
    #         if window[chr] >= need[chr]:
    #             valid_cnt += 1
    #     return valid_cnt
        
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

