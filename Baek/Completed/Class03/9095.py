import sys, math

def permutation(nums):
    # print(nums)
    n = 0
    for i in nums:
        n += nums[i]
    return int(math.factorial(n)/(math.factorial(nums[1])*math.factorial(nums[2])*math.factorial(nums[3])))

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())

    nums = {1:n, 2:0, 3:0}
    result = 0

    for i in range(n//3 + 1): # case '3'
        result += permutation(nums)
        while(True): # case '2'
            if nums[1] < 2:
                nums[1] += nums[2]*2
                nums[2] = 0
                break
            nums[2] += 1
            nums[1] -= 2
            
            result += permutation(nums)
        nums[1] -= 3
        nums[3] += 1
        
    print(result)