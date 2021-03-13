nums = [int(i) for i in input().split()]
n = len(nums)

if n > 1:
    for i in range(n-1):
        print(nums[i+1] + nums[i-1], end=' ')
        if i == n-2:
            print(nums[i] + nums[0], end=' ')
else:
    print(nums[0])