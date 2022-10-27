def merge_the_tools(string, k):
    # your code goes here
    s_lst = [string[i * k : (i+1) * k] for i in range(int(len(string)/k))]
    
    result_s_lst = list()
    for s in s_lst:
        result_lst = list(s)
        check_lst = list()
        for i in range(len(s)):
            if s[i] not in check_lst:
                check_lst.append(s[i])
                for j in range(i+1, len(s)):
                    if s[j] == s[i]:
                        result_lst[j] = ""
            else:
                continue
        result_s_lst.append("".join(result_lst))
    
    for result_s in result_s_lst:
        print(result_s)
