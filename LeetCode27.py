class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    print(s.removeElement(nums,val=2))