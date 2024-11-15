class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        cnt = {}

        for letter in s:
            cnt[letter] = cnt.get(letter, 0) + 1

        for letter in t:
            cnt[letter] = cnt.get(letter, 0) - 1

        for i in cnt.keys():
            if cnt[i] != 0:
                return False
        
        return True
