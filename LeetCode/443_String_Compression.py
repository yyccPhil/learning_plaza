class Solution:
    def compress(self, chars: List[str]) -> int:

        # Check Edge Case
        if len(chars) == 0:
            return len([''])
        
        if len(chars) == 1:
            return len(chars)
        
        res = []
        cnt = 1
        
        for i in range(len(chars) - 1):
            if chars[i] == chars[i+1]:
                cnt += 1
            else:
                res.append(chars[i])
                
                if cnt == 1:
                    pass
                elif cnt >= 10:
                    res.append(str(cnt//10))
                    res.append(str(cnt%10))
                else:            
                    res.append(str(cnt))
                cnt = 1
        
        # for last ele
        res.append(chars[-1])
        if cnt == 1:
            pass
        elif cnt >= 10:
            res.append(str(cnt//10))
            res.append(str(cnt%10))
        else:            
            res.append(str(cnt))
        
        return len(res)
        
