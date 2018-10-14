class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) == 1 or 0:
            return len(nums)
        else:
            while i+1 < len(nums):
                if nums[i] == nums[i+1]:
                    nums.pop(i+1)
                else:
                    i += 1
            return len(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2]
    print(s.removeDuplicates(nums))