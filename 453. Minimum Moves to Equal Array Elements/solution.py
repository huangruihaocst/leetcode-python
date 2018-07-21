class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        least = min(nums)
        return sum(i - least for i in nums)


if __name__ == '__main__':
    s = Solution()
    print(s.minMoves([1, 2, 3]))
