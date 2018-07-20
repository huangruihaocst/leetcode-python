class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        d = dict()
        for i in nums:
            d[i] = True
        res = list()
        for i in range(1, n + 1):
            if i not in d:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
