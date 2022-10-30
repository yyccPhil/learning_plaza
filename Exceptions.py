for i in range(int(input())):
    a, b = input().split()

    try:
        a = int(a)
        try:
            b = int(b)
            try:
                print(int(a/b))
            except ZeroDivisionError as e:
                print("Error Code: integer division or modulo by zero")
                # print("Error Code:", e) # Output -> Error Code: integer division or modulo by zero
        except ValueError as e:
            print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
