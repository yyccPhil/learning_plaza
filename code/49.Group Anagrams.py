#
# @lc app=leetcode id=49 lang=python3
# @lcpr version=20004
#
# [49] Group Anagrams
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res_lst = [[] for _ in range(len(strs))]
    #     letter_dict = dict()
    #     for i in range(len(strs)):
    #         if len(letter_dict) == 0:
    #             letter_dict[i] = self.letterLst(strs[i])
    #             res_lst[i].append(strs[i])
    #         else:
    #             for j in letter_dict.keys():
    #                 temp_letter_lst = letter_dict[j].copy()
    #                 flag = 1
    #                 for chr in strs[i]:
    #                     temp_letter_lst[ord(chr) - ord('a')] -= 1
    #                 for cnt in temp_letter_lst:
    #                     if cnt != 0:
    #                         flag = 0
    #                         break
    #                 if flag:
    #                     res_lst[j].append(strs[i])
    #                     break
    #             if not flag:
    #                 letter_dict[i] = self.letterLst(strs[i])
    #                 res_lst[i].append(strs[i])

    #     res = []
    #     for lst in res_lst:
    #         if len(lst) > 0:
    #             res.append(lst)
    #     return res
        
    # def letterLst(self, str1: str):
    #     letter_lst = [0 for _ in range(26)]
    #     for i in str1:
    #         letter_lst[ord(i) - ord('a')] += 1
    #     return letter_lst
        code_dict = dict()
        for s in strs:
            s_encode = self.encode(s)
            if s_encode not in code_dict.keys():
                code_dict[s_encode] = []
            code_dict[s_encode].append(s)

        return list(code_dict.values())
    
    def encode(self, str1: str):
        letter_lst = [0 for _ in range(26)]
        for i in str1:
            letter_lst[ord(i) - ord('a')] += 1
        return str(letter_lst)
        
# @lc code=end



#
# @lcpr case=start
# ["eat","tea","tan","ate","nat","bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

