class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr, cnt = None, 0
        for i in nums:
            if cnt == 0:
                curr = i
                cnt = 1
            else:
                if i == curr:
                    cnt += 1
                else:
                    cnt -= 1
        return curr


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3, 2, 3]))