
def print_formatted(number):
    # Manual binary, octal, hex
    def binary(b):
        b_list = list()
        i = b
        while i != 0:
            b_list.insert(0, "{}".format(i % 2))
            i //= 2
        return "".join(b_list)
    
    def octal(b):
        b_list = list()
        i = b
        while i != 0:
            b_list.insert(0, "{}".format(i % 8))
            i //= 8
        return "".join(b_list)
    
    def hexa(b):
        hexa_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15:"F"}
        b_list = list()
        i = b
        while i != 0:
            if i % 16 < 10:
                b_list.insert(0, "{}".format(i % 16))
            else:
                b_list.insert(0, hexa_dict[i % 16])
            i //= 16
        return "".join(b_list)
    
    l = len(binary(number))
    for i in range(1, number + 1):
        print("{}".format(i).rjust(l) + " " + octal(i).rjust(l) + " " + hexa(i).rjust(l) + " " + binary(i).rjust(l))
      
#     # Using built-in func
#     l = len(bin(number)[2:])
#     for i in range(1, number + 1):
#         print("{}".format(i).rjust(l) + " " + oct(i)[2:].rjust(l) + " " + hex(i)[2:].upper().rjust(l) + " " + bin(i)[2:].rjust(l))
            

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
