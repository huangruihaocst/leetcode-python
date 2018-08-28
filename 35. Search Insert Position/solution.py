class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Solution 1:
        # if not nums:
        #     return 0
        # for i, v in enumerate(nums):
        #     if v >= target:
        #         return i
        # return len(nums)

        # Solution 2: Binary Search
        left, right = 0, len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if target > nums[right]:
            return right + 1
        elif nums[left] < target <= nums[right]:
            return right
        elif target <= nums[left]:
            return left


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 6))
