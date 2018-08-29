class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _sum = sum(nums)
        left = 0  # sum of the numbers left to the current number
        for i, v in enumerate(nums):
            if left == _sum - v - left:
                return i
            left += v
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([1, 2, 3]))
