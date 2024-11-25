import sys
input = sys.stdin.read

def main():

    input_cnt = 0
    input_data = input().split()

    nums_len = int(input_data[0])
    input_cnt += 1

    nums = list()
    for i in range(input_cnt, input_cnt + nums_len):
        nums.append(int(input_data[i]))

    input_cnt += nums_len

    for i in range(nums_len-1):
        nums[i+1] += nums[i]

    for i in range(input_cnt,len(input_data),2):
        start = int(input_data[i])
        end = int(input_data[i+1])
        if start > 0:
            print(nums[end] - nums[start - 1])
        else:
            print(nums[end])

if __name__ == "__main__":
    main()

