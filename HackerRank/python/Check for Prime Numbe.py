## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

# cnt = 0
# for num in check_prime:
#     for i in range(2, num):
#         if num % i == 0:
#             print("{} is NOT a prime number, because {} is a factor of {}".format(num, i ,num))
#             cnt += 1
#             break
#     if cnt == 0:
#         print("{} IS a prime number.".format(num))



# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# that's best!!!
# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))
