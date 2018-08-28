class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sum(nums)
        delta = s - len(nums) * (len(nums) + 1) // 2  # equals to (duplicate number - missed number)
        occurs = set()
        duplicate = -1
        for i in nums:
            if i not in occurs:
                occurs.add(i)
            else:
                duplicate = i
                break
        return [duplicate, duplicate - delta]


if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums([1, 2, 2, 4]))
