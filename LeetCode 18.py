nums = [-3,-2,-1,0,0,1,2,3]
nums.sort()
target = 0
num_save = []

if len(nums) < 4 or nums == []:
    print([[]])
else:
    if len(nums) == 4 and sum(nums) == target:
        num_save.append(nums)
        print(num_save)
    else:
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                l = j+1
                r = len(nums) - 1
                while l < r:
                    sums = nums[i] + nums[j] + nums[l] + nums[r]
                    if sums == target:
                        num_save.append([nums[i], nums[j], nums[l], nums[r]])
                        break
                    elif sums < target:
                        l += 1
                    else:
                        r -= 1
        num_save = list(set([tuple(t) for t in num_save]))
        print(num_save)