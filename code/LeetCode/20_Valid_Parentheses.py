class Solution:
    def isValid(self, s: str) -> bool:

        # Check Edge Case
        if len(s)%2 != 0:
            return False
        
        open_paren = set('([{')
        match_paren = set([('(',')'),('[',']'),('{','}')])

        judge_stack = list()

        for i in s:
            if i in open_paren:
                judge_stack.append(i)
            else:
                # in case the first parens is closing
                if len(judge_stack) == 0:
                    return False
                    
                if (judge_stack.pop(), i) not in match_paren:
                    return False

        # in case all parens are opening
        if len(judge_stack) == 0:
            return True
        else:
            return False

