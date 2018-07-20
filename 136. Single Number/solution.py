class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i in nums:
            d[i] = d[i] + 1 if i in d else 1
        for i in d:
            if d[i] == 1:
                return i


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))
