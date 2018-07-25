class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        if nums[0] >= 0 or nums[-1] <= 0:  # all positive or all negative
            return nums[-1] * nums[-2] * nums[-3]
        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])