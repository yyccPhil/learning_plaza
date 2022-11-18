# A good way to check the regex for errors

import re

for i in range(int(input())):
    try:
        re.compile(r"{}".format(input()))
        print(True)
        # print(bool(re.compile(r"{}".format(input()))))
    except re.error:
        print(False)
