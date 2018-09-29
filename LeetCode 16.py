nums = [0, 2, 1, -3]
target = 1
temp = float('inf')
if len(nums) == 3:
    print(sum(nums))
else:
    for i in range(len(nums)-2):
        for l in range(i+1, len(nums)-1):
            r = len(nums) - 1
            while l < r:
                sums = nums[i] + nums[l] + nums[r] - target
                if abs(sums) < abs(temp):
                    temp = sums
                r -= 1

    print(temp+target)