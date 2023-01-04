
if __name__ == '__main__':
    s_dict = dict()
    for i in input():
        s_dict[i] = s_dict.get(i, 0) + 1
    for char, n in sorted(s_dict.items(), key = lambda x: (-x[1], x[0]))[:3]:
        print(char, n)

# Note: sorted() and .sort() have 3 arguments:
# iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
# reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
# key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.
# Especially key! It likes map(), to operate iterable with a func, like lambda x: x[0], for sequentially sorting, can use like (x[0], x[1]).
