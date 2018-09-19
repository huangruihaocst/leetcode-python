class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        for i in range(len(nums)):
            if i == 0:
                continue
            if (i % 2 == 0 and nums[i] > nums[i - 1]) or (i % 2 == 1 and nums[i] < nums[i - 1]):
                swap(i, i - 1)


if __name__ == '__main__':
    s = Solution()
    li = [3, 5, 2, 1, 6, 4]
    s.wiggleSort(li)
    print(li)
