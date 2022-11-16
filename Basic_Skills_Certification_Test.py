# Missing Characters

def missingCharacters(s):
    # Write your code here
    char_lst = [chr(ord('a') + i) for i in range(26)]
    dig_lst = [str(i) for i in range(10)]
    for i in list(s):
        if i in char_lst or i in dig_lst:
            if i in char_lst:
                char_lst.remove(i)
            else:
                dig_lst.remove(i)
    return "".join(dig_lst) + "".join(char_lst)

# -----------------------------------------------------------  
  
# Average Function

def avg(*nums):
    return sum(nums)/len(nums)
