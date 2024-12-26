#
# @lc app=leetcode id=150 lang=python3
# @lcpr version=20004
#
# [150] Evaluate Reverse Polish Notation
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = list()
        for c in tokens:
            # 判断是否为数字，因为isdigit()不识别负数，故需要排除第一位的符号
            if c.isdigit() or (len(c)>1 and c[1].isdigit()):
                my_stack.append(c)
            else:
                y = my_stack.pop()
                x = my_stack.pop()
                my_stack.append(str(int(eval(x+c+y))))
        return int(my_stack[0])
    
        
# @lc code=end



#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#

