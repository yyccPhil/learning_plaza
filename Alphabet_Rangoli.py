# def print_rangoli(size):
#     # your code goes here
#     alpha_list = [chr(i) for i in range(97,123)]
    
#     # v1
#     # first line
#     print(alpha_list[size - 1].center(4 * size - 3, "-"))
    
#     # top half
#     for i in range(size - 1):
#         c_list = list()
#         for j in range(size - 1, size - 3 - i, -1):
#             c_list.append(alpha_list[j])
#         for k in range(size - 1 - i, size):
#             c_list.append(alpha_list[k])
#         print("-".join(c_list).center(4 * size - 3, "-"))
    
    
    
#     # v2
#     # top half
#     for i in range(size):
#         c_list = list()
#         for j in range(size - 1, size - 2 - i, -1):
#             c_list.append(alpha_list[j])
#         for k in range(size - i, size):
#             c_list.append(alpha_list[k])
#         print("-".join(c_list).center(4 * size - 3, "-"))


def print_rangoli(size):
    # your code goes here
    alpha_lst = [chr(i) for i in range(97,123)]
    
    # top half
    top_lst = list()
    for i in range(size):
        c_lst = list()
        for j in range(size - 1, size - 2 - i, -1):
            c_lst.append(alpha_lst[j])
        c_lst += list(reversed(c_lst))[1:]
        # for k in range(size - i, size):
        #     c_lst.append(alpha_lst[k])
        print("-".join(c_lst).center(4 * size - 3, "-"))
        top_lst.append(c_lst)
    
    # bottom half
    for i in range(size - 2, -1 ,-1):
        print("-".join(top_lst[i]).center(4 * size - 3, "-"))
            

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
